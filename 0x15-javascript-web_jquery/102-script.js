$('document').ready(function () {
  $('INPUT#btn_translate ').click(function () {
    const lang = $('INPUT#language_code').val();
    fetch(lang);
  });
});

function fetch (txt) {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=' + txt, function (data, status) {
    $('DIV#hello').text(data.hello);
  });
}
