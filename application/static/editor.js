var canvas = document.querySelector("canvas");
var tilesetContainer = document.querySelector(".tileset-container");
var tilesetSelection = document.querySelector(".tileset-container_selection");
var tilesetImage = document.querySelector("#tileset-source");
let importedLevel = document.querySelector('input');
var newData = "";



var selection = [0, 0]; //Which tile we will paint from the menu

var isMouseDown = false;
var currentLayer = 0;
var layers = [
   // Grid, keep empty
   {

   }
];

//Select tile from the Tiles grid
tilesetContainer.addEventListener("mousedown", (event) => {
   selection = getCoords(event);
   tilesetSelection.style.left = selection[0] * 32 + "px";
   tilesetSelection.style.top = selection[1] * 32 + "px";
});

//Handler for placing new tiles on the map
function addTile(mouseEvent) {
   var clicked = getCoords(event);
   var key = clicked[0] + "-" + clicked[1];

   if (mouseEvent.shiftKey) {
      delete layers[currentLayer][key];
   } else {
      layers[currentLayer][key] = [selection[0], selection[1]];
     
   }
   draw();

}

//Bind mouse events for painting (or removing) tiles on click/drag
canvas.addEventListener("mousedown", () => {
   isMouseDown = true;
});
canvas.addEventListener("mouseup", () => {
   isMouseDown = false;
});
canvas.addEventListener("mouseleave", () => {
   isMouseDown = false;
});
canvas.addEventListener("mousedown", addTile);
canvas.addEventListener("mousemove", (event) => {
   if (isMouseDown) {
      addTile(event);
   }
});

//Utility for getting coordinates of mouse click
function getCoords(e) {
   const { x, y } = e.target.getBoundingClientRect();
   const mouseX = e.clientX - x;
   const mouseY = e.clientY - y;
   return [Math.floor(mouseX / 32), Math.floor(mouseY / 32)];
}

// download levels for importing
function exportImage() {
   draw();

   // data = data.replace(/\D/g, '');
   gdlevel = "";
   currentNum = "";
   x = false;


   console.log(data + " - The data");
   for (var i = 0; i < data.length + 1; i++) {
      console.log(data[i] + " - i");
      if (data[i] == "-" || data[i] == "," || data[i] == null) {
         x = !x;
         if (x == true){
            console.log(currentNum + " - x coord");
            gdlevel = gdlevel.concat("1," + blockType + ",2," + currentNum + ",");
         }
         else {
            console.log(currentNum + " - y coord");
            gdlevel = gdlevel.concat("3," + currentNum + ";");  
         }
         currentNum = "";  
      }
      else {
         currentNum = currentNum.concat(data[i]);
      }
      
   }


   

   

   // gdlevel = gdlevel.substring(0, gdlevel.length - 1);
   vaildLevel = false;
   while (vaildLevel == false){
      lvlName = window.prompt("Level Name (20 Characters limit):")
      lvlName = lvlName.replace(/[^a-zA-Z0-9 ]/gi,'');

      if (lvlName.length > 20) {
         window.alert("Too Long")
   
      }
      else if (lvlName.length <= 0){
         lvlName = "Unnamed";
         vaildLevel = true;
      }
      else {
         vaildLevel = true;
      }
   }

   

   download(lvlName,gdlevel); 
   console.log(gdlevel + " - The level");


   
}

//Reset state to empty
function clearCanvas() {
   layers = [{}, {}, {}];
   draw();
}

function setLayer(newLayer) {
   //Update the layer
   currentLayer = newLayer;

   //Update the UI to show updated layer
   var oldActiveLayer = document.querySelector(".layer.active");
   if (oldActiveLayer) {
      oldActiveLayer.classList.remove("active");
   }
   document.querySelector(`[tile-layer="${currentLayer}"]`).classList.add("active");
}

function draw() {
   var ctx = canvas.getContext("2d");
   ctx.clearRect(0, 0, canvas.width, canvas.height);

   var size_of_crop = 32;
   
   layers.forEach((layer) => {
      Object.keys(layer).forEach((key) => {
         
         
         
         //Determine x/y position of this placement from key ("3-4" -> x=3, y=4)
         var positionX = Number(key.split("-")[0]);
         var positionY = Number(key.split("-")[1]);
         var [tilesheetX, tilesheetY] = layer[key];

         

         data = Object.keys(layer).toString();
         blockType = (tilesheetX + tilesheetY * 6) + 1;

         var id = "ctl03_Tabs1";
         var curBlock = data.substr(id.length - 5);


         console.log(data);

         ctx.drawImage(
            tilesetImage,
            tilesheetX * 32,
            tilesheetY * 32,
            size_of_crop,
            size_of_crop,
            positionX * 32,
            positionY * 32,
            size_of_crop,
            size_of_crop
         );
      });
   });
}


//Initialize app
tilesetImage.onload = function() {
   layers = defaultState; // default state empty
   draw();
   setLayer(0);
}


// download as text file
function download(filename, text) {
   var element = document.createElement('a');
   element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
   element.setAttribute('download', filename);
 
   element.style.display = 'none';
   document.body.appendChild(element);
 
   element.click();
 
   document.body.removeChild(element);
 }

 // make converter thingy
 function encode()
 {
    
 }


