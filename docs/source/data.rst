Data
====

The 'standardized' data represents meter readings in an XML format that is derived from the Energy Star Portfolio Manager (ESPM) XML exchange formats.
This is the format used by external connectors to feed data.

Hourly 'standardized' data is stored per data point, with each data point stored in a separate XML file together with a reference to description of the corresponding meter configuration, 
time period, and meta-information, similar to the following example:

.. code-block:: xml

  <?xml version='1.0' encoding='UTF-8'?>
  <bm:meterData xmlns:bm="http://benchmark8760.com/ns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:espm="http://portfoliomanager.energystar.gov/ns" xsi:schemaLocation="http://benchmark8760.com/ns http://benchmark8760.com/ns/main.xsd">
    <bm:meteredData>
      <bm:meterURI>participant_1/config/meter_occupancy.xml</bm:meterURI>
      <bm:startTime>2021-12-22T12:00:00</bm:startTime>
      <bm:endTime>2021-12-22T13:00:00</bm:endTime>
      <bm:usage>7</bm:usage>
      <bm:audit>
        <espm:createdBy>Occupancy Connector</espm:createdBy>
        <espm:createdDate>2022-03-18T09:33:24</espm:createdDate>
      </bm:audit>
    </bm:meteredData>
  </bm:meterData>

All times are in UTC, starting and including the `bm:startTime` up to but excluding the `bm:endTime`. The above snippet represents an occupancy meter reading of 7 
for the period of one hour starting at noon on December 22, 2021. The meter was read much later, on March 18, 2022 as recorded in the `bm:audit` section.