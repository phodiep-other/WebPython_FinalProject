%def searchresults():

  <h3>Search Parameters:</h3>

  <p>Location: <em>{{location}}</em><br>
     Bedrooms: {{bed}}<br>
     Rent (min): {{rentmin}}<br>
     Rent (max): {{rentmax}}<br><br>
     Thanks for searching!<br><br>
     <hr>
     
%for entry in results:
	<div style="float: right"><a href="http://maps.google.com/?cbll={{entry['loc_lat']}},{{entry['loc_long']}}&cbp=12,20.09,,0,5&layer=c"><img src="http://maps.googleapis.com/maps/api/streetview?size=200x200&location={{entry['loc_lat']}},{{entry['loc_long']}}&sensor=false&key=AIzaSyB-2CXs-Ia0KQTspr-vlzr5QGGckp0UEAM"></a></div>
	ID: {{entry['ID']}}<br>

        Title: <a href="{{entry['post_url']}}">{{entry['title']}}</a><br>
  
        Header: {{entry['header']}}<br>

	Neighborhood: {{entry['neighborhood']}}<br>

	Latitude: {{entry['loc_lat']}}<br>

	Longitude: {{entry['loc_long']}}<br>

	
	<br>
<br><br><br><br><hr>
        %end

%end



%rebase layout.tpl title='Search Results', body=searchresults