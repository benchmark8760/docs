Architecture
============

The platform is architected as a cloud-native serverless solution built for Google Cloud Platform (GCP), 
relying on Google Cloud Storage buckets for all its storage and on BigQuery for combining collected data for analytics.

The platform serves platform participants, and for each participant a special user group is created in Google Admin, holding users related to this participant. 
Also, for each participant a separate GCP cloud storage bucket is created to host participant's configuration and data, with its access generally restricted to the corresponding user group. 

Every hour platform scheduler is invoking platform dispatcher, a cloud function that is responsible for iterating through all participants, reading their configurations, and invoking the necessary connectors to fetch meter data.

The connectors are also implemented as cloud functions, parameterized, and invoked to fetch data for specific meters, configured by specific participants. The connectors are producing hourly data for each meter, keeping log of raw data as fetched from the meter, and performing all actions necessary to fetch, convert, aggregate or interpret the raw data to obtain per-hour meter readings that are also referred to as 'standardized' data.

Then the hourly data is further aggregated per type of data to form the final hourly measurements of each type of data that are loaded into the data warehouse. In this way, for example, per-minute data coming from several occupancy censors installed in different areas of a building are combined to estimate the total occupancy at each hour.


.. figure:: top-level-architecture.png
   :width: 100%

   Architecture overview of the system
 

Shared Core
-----------

The shared core of the platform is responsible for invoking data connectors every hour and to load the collected the 'standardized' data into the data warehouse.

The converters themselves are responsible for fetching the data from a specific data source each, resolve all technical and data interpretation issues, and store the data on GCP cloud storage in teh so-called 'standardized' format.


Connectors
---------- 

Platform data connectors are internal to the platform, implemented and deployed as cloud functions.
All connectors are configured with XML files stored on GCP cloud storage buckets of the appropriate platform participants. 
The shared core is parsing these configurations to determine which cloud functions need to be invoked and with which parameters. 

External connectors are not deployed with the platform, but are deployed externally and send standardized data directly to the GCP cloud storage buckets using the GCP cloud storage REST API. 
They are not invoked by the shared core, and they are not configured in XML as invokable cloud functions. 


Drop box
--------

To ensure security external connectors are feeding the data into a special GCP storage bucket called 'dropbox'. The platform is then picking that data up and copying it to the appropriate locations for 'standardized' data.

Data Warehouse
--------------

Metered data is put into the context of the meters that provide the data and the properties that are being metered. The bare metered numbers are then interpreted given:

+ type of metered data: as property electricity consumption, property occupancy, expected CO2 emissions given the type of electricity supply contract, weather conditions such as temperature
+ regional information about office hours, holidays, office closures, etc.
+ derived metrics, such as the difference between interanl and ambient temperature that has to be achieved. 

Meters and property to meter association is configured in XML for both, internal and external connectors. 

Both, configuration data and metered data, is loaded into the data warehouse as illustrated with the following figure:

.. figure:: data-flow-connectors-aggregators.png
   :width: 100%

   Data and configuration flow

All this data is then analyzed with Google Data Studio to formualte and assess various energy benchmarking formulas.
 