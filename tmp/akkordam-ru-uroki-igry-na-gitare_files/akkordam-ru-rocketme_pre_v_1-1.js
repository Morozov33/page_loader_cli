document.addEventListener("DOMContentLoaded", function(){
	var style = document.createElement('style');
	style.innerHTML = '.rocketme_pre{opacity:0!important;visibility: hidden!important;}';
	document.getElementsByTagName('head')[0].appendChild(style);	
	let elements = document.querySelectorAll('iframe, .rocketme_video');
	for (let elem of elements) {
		elem.classList.add("rocketme_pre");
	}
	setTimeout(function(){
		let elements = document.querySelectorAll('.rocketme_pre');
		for(let elem of elements){
			elem.classList.remove("rocketme_pre");
		}
	},3000);
})