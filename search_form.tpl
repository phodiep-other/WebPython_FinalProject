%def searchform():
  <form method="POST" action="/search">
  Location<br><input name="location" type="text" /><br><br>
  Min # Beds<br><input name="bed" type="number"  /><br><br>
  Rent min<br><input name="rentmin" type="number"/><br><br>
  Rent max<br><input name="rentmax" type="number"/><br><br>
  <input type="submit" />
  </form>
%end

%rebase layout.tpl title='Search for Apartments in Seattle', body=searchform