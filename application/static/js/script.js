$(document).ready(function() {
    console.log('document loaded');
    $('.application').on('click', function() {
		var app=$(this).attr('name');
		window.location = '/catalog/'+app+'/details';
	});
	$('#cloud-link').click(function(){
	    console.log('Launch In The Cloud');
	    name=$('#cloud-link').data('label');
//	    window.location='/catalog/'+name+'/launch';
	});
	$('#compose-link').click(function(){
	    console.log('Download Compose');
	});
	$("#search-bar").on("keyup", function() {
	    console.log('Search Bar working');
        var g = $(this).val().toLowerCase();
        console.log(g);
        $(".application h4 a").each(function() {
            var s = $(this).text().toLowerCase();
            $(this).closest('.application')[ s.indexOf(g) !== -1 ? 'show' : 'hide' ]();
        });
    })
});