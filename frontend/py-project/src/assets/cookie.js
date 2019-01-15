export function setCookie(c_name,value,expire){
	var date=new Date()
	date.setSecond(date.getSeconds()+expire)
	document.cookie=c_name+""+escape(value)+

E4624427813dd


}