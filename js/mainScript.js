var Border = false;
//loadTable1();

//Function to set active to the active <li> in sidebar
function navActive(num){
	var ul = document.getElementById("lista");
	var items = ul.getElementsByTagName("li");
	for (var i = 0; i < items.length; ++i) {
		items[i].className = "";
	}
	var item = document.getElementById( "pf" + parseInt(num) );
	item.className = "active";
}

//Function to show divs from the nav menu
function showDiv(divNum)
{
	navActive(divNum);
	
	var divs = document.getElementById("content");
	var div = divs.getElementsByTagName("div");
	for (var i = 0; i < div.length; ++i) {
		div[i].style.display = "none";
	}
	var show = document.getElementById("div" + parseInt(divNum));
	show.style.display = "";
}

async function loadTable1(){
	const pf = await import( "../json/portfolios.json", {
		assert: {
			type: 'json'
		}
	});
	var portFolios = pf.default.PortFolios;
	var tbody = document.getElementById("tbody1");
	for(var i = 0; i < portFolios.length; i++) {
		var tr = document.createElement("tr");
		var td1 = document.createElement("td");
		td1.appendChild(document.createTextNode(portFolios[i].pfName));
		tr.appendChild(td1);
		var td2 = document.createElement("td");
		td2.appendChild(document.createTextNode(portFolios[i].tickers));
		tr.appendChild(td2);
		tbody.insertBefore( tr, tbody.lastElementChild);
	}
}

function showBorder(){
	if(!Border){
		var top = document.getElementById("pageTopBorder");
		top.style.display = "block";
		var right = document.getElementById("pageRightBorder");
		right.style.display = "block";
		var bot = document.getElementById("pageBotBorder");
		bot.style.display = "block";
		Border = true;
	}
	else{
		var top = document.getElementById("pageTopBorder");
		top.style.display = "none";
		var right = document.getElementById("pageRightBorder");
		right.style.display = "none";
		var bot = document.getElementById("pageBotBorder");
		bot.style.display = "none";
		Border=false;
	}
}   