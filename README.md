# Distance By Zipcode API
 
<h2>Python-flask API to get distance between pair of zip codes</h2>
<h2>Dependencies</h2>
<a href="https://pypi.org/project/Flask/">Flask</a>: for the web framework<br />
<a href="https://pypi.org/project/pandas/">Pandas</a>: to interact with the datasest<br />
<a href="https://pypi.org/project/geopy/">Geopy</a>: calculate distance between coordinates<br />
<a href="https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/table/"> US Zip Code Latitude and Longitude</a>: lookup coordinates from zip code<br />
<br /><h2>Usage</h2>

1. Run the DistanceByZips_API_DRIVER.py
2. Go to <a href="127.0.0.1:5000/?zip1=90001&zip2=10020">127.0.0.1:5000/?zip1=90001&zip2=10020</a> (replace zip codes with ones you are looking to calculate)<br /> 
3. Result is a JSON file:

<pre><code>{
  "distance_Km": 3936.720999605038, 
  "distance_Mi": 2446.1650210303314, 
  "zip1": "90001", 
  "zip2": "07452"
}</code></pre>
4. Invalid zip codes return a null value.

Further documentation can be found through Flask, Pandas, and Geopy
