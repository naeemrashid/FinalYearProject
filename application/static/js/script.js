$(document).ready(function() {
    console.log('document loaded');
    $('.application').on('click', function() {
		var app=$(this).attr('name');
		window.location = '/catalog/'+app+'/details';
	});
	$('#cloud-link').click(function(){
	    console.log('Launch In The Cloud');
	});
	$('#compose-link').click(function(){
	    console.log('Download Compose');
	});
});