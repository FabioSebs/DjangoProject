let tlForm = new TimelineLite;

tlForm.to("#loginForm" , 0.5 , {opacity: 0.8 , ease: Power4})
.to("#formLogo" , 1.3 , {scaleX: 1.3 , scaleY: 1.3 , ease: Back.easeOut.config(8)});