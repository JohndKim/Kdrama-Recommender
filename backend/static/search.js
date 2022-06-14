d3.csv('..\\static\\kdrama_data.csv').then(function (data) {
  console.log(data);

  var kdrama = data;

  var button = d3.select('#button');

  var form = d3.select('#form');

  button.on('click', runEnter);
  form.on('submit', runEnter);

  function runEnter() {
    // clears previous table if there is one
    d3.select('tbody').html('');
    // prevents reload
    d3.event.preventDefault();
    var inputElement = d3.select('#user_input');
    var inputValue = inputElement.property('value');
    // .toLowerCase().trim()

    console.log(inputValue.length);

    var filteredData = kdrama.filter((kdrama) => kdrama.title.trim().includes(inputValue));

    var output = _.sortBy(filteredData, 'title').reverse();

    for (var i = 0; i < filteredData.length; i++) {
      d3.select('tbody')
        .insert('tr')
        .html(
          '<td>' +
            [i + 1] +
            '</td>' +
            '<td>' +
            '<a href=https://www.imdb.com/title/' +
            output[i]['rank'] +
            " target='_blank'>" +
            output[i]['title'] +
            '</a>' +
            '</td>' +
            '<td>' +
            output[i]['ep'] +
            '</td>' +
            '<td>' +
            output[i]['duration'] +
            '</td>' +
            '<td>' +
            output[i]['content_rating'] +
            '</td>' +
            '<td>' +
            output[i]['description'] +
            '</td>'
        );
    }
  }
  //   window.resizeTo(screen.width, screen.height);
});
