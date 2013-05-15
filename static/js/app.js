/*!
 * App JS v1.0
 *
 * Licensed under the Apache License v2.0
 * http://www.apache.org/licenses/LICENSE-2.0
 */

function toggle_visibility(id) {
	var e = document.getElementById(id);
	if(e.style.display == 'none')
		e.style.display = 'inline';
	else
		e.style.display = 'none';
}

 // On Page Load
 $(function() {

 	$('#list').click(function () {
 			toggle_visibility('#menu');
 		});

});