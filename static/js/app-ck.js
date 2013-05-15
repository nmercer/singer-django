/*!
 * App JS v1.0
 *
 * Licensed under the Apache License v2.0
 * http://www.apache.org/licenses/LICENSE-2.0
 */function toggle_visibility(e){var t=document.getElementById(e);t.style.display=="none"?t.style.display="inline":t.style.display="none"}$(function(){$("#list").click(function(){toggle_visibility("#menu")})});