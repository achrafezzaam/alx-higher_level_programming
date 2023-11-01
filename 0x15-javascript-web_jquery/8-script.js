$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  for (const elem in data.results) {
    $('UL#list_movies').append('<li>' + data.results[elem].title + '</li>');
  }
});
