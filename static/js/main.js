function stem(){
    $.ajax({
      type: "POST",
      url: "/stem/",
      dataType: 'json',
      data: JSON.stringify({ "text": $('#input_text').val()})
    })
    .done(function(data) {
        $('#output_text').text(data['output']);
    });
}
$(document).ready(function() {
    $('#btn-stem').click(function( event ) {
        event.preventDefault();
        stem();
    });
});