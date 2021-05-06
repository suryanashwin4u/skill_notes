      			  javascript notes
--------------------------------------------
//change the inner html string using id selector
document.getElementById("id_name").innerHTML = "type_string_here";

//can be declared like this
document.getElementById("demo").innerHTML =
"Hello Dolly!";

//calculate and print
document.getElementById("demo").innerHTML = 5 + 6;

//print at browser window
document.write("type_string_here");

//calculate and print
document.write(5 + 6);

//to show alert message
alert(5 + 6);

//to show alert message
window.alert("helloworld");

//to print at console
console.log("helloworld");

//change src attribute using id selector
document.getElementById("id_name").src='image.gif';

//change styles using id selector
document.getElementById("demo").style.fontSize = "35px";

//to hide element using id selector
document.getElementById("demo").style.display = "none";

//to show element using id selector
document.getElementById("demo").style.display = "block";

//include script from same folder
<script src="myScript.js"><script>

//include script from other server
<script src="https://www.w3schools.com/js/myScript1.js"><script>

//include script from different folder in same directory
<script src="/js/myScript1.js"><script>

//define function in js and include in the same page
<script>
function myFunction() {
  document.getElementById("demo1").innerHTML = "Hello Dolly!";
  document.getElementById("demo2").innerHTML = "How are you?";
}
<script>

//click button , calculate and then print
<button type="button" onclick="document.write(5 + 6)"><button>

//click button and print on screen
<button onclick="window.print()"><button>


//declare variables
var x, y, z;    
x = 5;        
y = 6;          
z = x + y;  
var person = "Hege";
var person='Hege';
var x = y + z;

//looks same but different variables as of upper case letter
var lastname, lastName;
lastName = "Doe";
lastname = "Peterson";


//general rules for creating variables:
.Names can contain letters, digits, underscores, and dollar signs
.Names must begin with a letter
.Names can also begin with $ and _
.Names are case sensitive
.keywords cannot be used as variable names

//declare many variables on the same line and ending with semicolon
var person = "John Doe", carName = "Volvo", price = 200;

//declare many variables using comma on different lines and ending with semicolon
var person = "John Doe",
carName = "Volvo",
price = 200;

//undefined variable
var carName;

//calculations or string concatenation from left to right
var x = 5 + 2 + 3;
var x = "John" + " " + "Doe";
var x = "5" + 2 + 3;
var x = 2 + 3 + "5";

//dollars can be used as identifiers
var $$$ = "Hello World";
var $ = 2;
var $myvar=10;


//underscore can be used as an identifier
var _lastName = "Johnson";
var _x = 2;
var _100 = 5;


//var variables cannot restrict access outside the block
var x = 10;
// Here x is 10
{
  var x = 2;
  // Here x is 2
}
// Here x is 2


var i = 5;
for (var i = 0; i < 10; i++) {
// some statements
}
// Here i is 10


//let helps restrict access outside the block
var x = 10;
// Here x is 10
{
  let x = 2;
  // Here x is 2
}
// Here x is 10


//both let and var has global scope
let i = 5;
var y=5;
for (let i = 0; i < 10; i++){

}
// Here i and y are 5


//both var or let declared inside function have only function scope
function myFunction() {
  var carName = "Volvo";   // Function Scope
  let carName = "Volvo";   // Function Scope
}


//var variables can be accessed with windows object but with let we cannot do the same
var carName = "Volvo";
window.carName;


//redeclaring a var variable using let is not allowed
var x = 2;       // Allowed
let x = 3;       // Not allowed
{
  var x = 4;   // Allowed
  let x = 5   // Not allowed
}


//redeclaring let variables is not allowed in the same block
let x = 2;       // Allowed
let x = 3;       // Not allowed
{
  let x = 4;   // Allowed
  let x = 5;   // Not allowed
}

//redeclaring a let variable using var variable is not allowed
let x = 2;       // Allowed
var x = 3;       // Not allowed
{
  let x = 4;   // Allowed
  var x = 5;   // Not allowed
}


//different scopes is possible using let 
let x = 2;     // Allowed
{
  let x = 3;   // Allowed
}
{
  let x = 4;   // Allowed
}


//cant use let after assignment 
try {
  carName = "Volvo";	
  let carName;			//not allowed
  document.getElementById("demo").innerHTML = carName;
}
catch(err) {
//err object
  document.getElementById("demo").innerHTML = err.name + ":" + err.message;
}


//cant be reassigned
const PI = 3.141592653589793;
PI = 3.14;      // error
PI = PI + 10;   // error


//scope of const works same like let
var x = 10;
// Here x is 10
{
  const x = 2;
  // Here x is 2
}
// Here x is 10


//const variables should be assigned inline directly
const PI = 3.14159265359;


//object values can be changed even declared with const
const car = {type:"Fiat", model:"500", color:"white"};
car.color = "red";
car.owner = "Johnson";

//const object once defined cant be reassigned
const car = {type:"Fiat", model:"500", color:"white"};
CAR = {type:"Volvo", model:"EX60", color:"red"};    // ERROR


//const arrays can be updated and not reassigned
const cars = ["Saab", "Volvo", "BMW"];
cars[0] = "Toyota";
cars.push("Audi");


//const array cant be reassigned
const cars = ["Saab", "Volvo", "BMW"];
CARS = ["Toyota", "Volvo", "Audi"];    // ERROR


//reassigning const values is not allowed
var x = 2;         // Allowed
const x = 2;       // Not allowed
{
  let x = 2;     // Allowed
  const x = 2;   // Not allowed
}


//redeclaration is not allowed in same scope
const x = 2;       // Allowed
const x = 3;       // Not allowed
x = 3;             // Not allowed
var x = 3;         // Not allowed
let x = 3;         // Not allowed
{
  const x = 2;   // Allowed
  const x = 3;   // Not allowed
  x = 3;         // Not allowed
  var x = 3;     // Not allowed
  let x = 3;     // Not allowed
}


//const can be declared like let in different blocks
const x = 2;     // Allowed
{
  const x = 3;   // Allowed
}
{
  const x = 4;   // Allowed
}

//const declared after assignment will produce error
carName = "Volvo";
const carName;		//not allowed


//string concatenation
var txt1 = "John";
var txt2 = "Doe";
var txt3 = txt1 + " " + txt2;	

var txt1 = "What a very ";
txt1 += "nice day";

var y = "5" + 5;			//55
var z = "Hello" + 5;		//Hello5
var x = 16 + "Volvo";		//16Volvo
var x = "16" + "Volvo";		//16Volvo
var x = 16 + 4 + "Volvo";   //20Volvo
var x = "Volvo" + 16 + 4;   //Volvo20


//exponentation works like pow function in Math class
var x = 5;
var z = x ** 2;          // result is 25
var z = Math.pow(x,2);   // result is 25

//using single and double quotes
var carName1 = "Volvo XC60";   			  // Using double quotes
var carName2 = 'Volvo XC60';   			  // Using single quotes
var answer1 = "It's alright";             // Single quote inside double quotes
var answer2 = "He is called 'Johnny'";    // Single quotes inside double quotes
var answer3 = 'He is called "Johnny"';    // Double quotes inside single quotes
var y = 123e5;      					  // 12300000
var z = 123e-5;     					  // 0.00123



//returns true or false
(x == y)       // Returns true
(x == z)       // Returns false


//array declaration
var cars = ["Saab", "Volvo", "BMW"];


//objects declaration
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
//or
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

//method without the () parentheses, it will return the function definition
document.getElementById("demo").innerHTML = person.fullName;

//accessing objects
objectName.propertyName;
//or
objectName["propertyName"];

//try not to use objects as it slows down the execution
var x = new String();        // Declares x as a String object
var y = new Number();        // Declares y as a Number object
var z = new Boolean();       // Declares z as a Boolean object


//type of returns datatype
typeof ""             		 // Returns "string"
typeof "John"                // Returns "string"
typeof "John Doe"            // Returns "string"
typeof 0                     // Returns "number"
typeof 314                   // Returns "number"
typeof 3.14                  // Returns "number"
typeof (3)                   // Returns "number"
typeof (3 + 4)               // Returns "number"
typeof true                  // Returns "boolean"
typeof false                 // Returns "boolean"
typeof x                     // Returns "undefined" 
typeof undefined             // Returns "undefined"
typeof null                  // Returns "object"
typeof {name:'John', age:34} // Returns "object"
typeof [1,2,3,4]             // Returns "object" 
typeof function myFunc(){}   // Returns "function"


// Value is undefined, type is undefined
var car;    
car = undefined;


// The value is "", the typeof is "string"
var car = "";    


//null is an object type
person = null;   


//null value and type is undefined here
person=undefined;

//check null or undefined
null === undefined         // false
null == undefined          // true


//accessing a function without () will reassing the code at the give function name
function toCelsius(f) {
  return (5/9) * (f-32);
}
document.getElementById("demo").innerHTML = toCelsius; //it will assign function defination here


//local variable inside the function
function myFunction() {
  var carName = "Volvo";
  // code here CAN use carName
}

//event onclick
<button onclick="document.getElementById('demo').innerHTML = Date()">The time is?<button>
<button onclick="this.innerHTML = Date()">The time is?<button>
<button onclick="displayDate()">The time is?<button>


Event				Description
-----------------------------------------------------------------
onchange	|	An HTML element has been changed
onclick		|	The user clicks an HTML element
onmouseover	|	The user moves the mouse over an HTML element
onmouseout	|	The user moves the mouse away from an HTML element
onkeydown	|	The user pushes a keyboard key
onload		|	The browser has finished loading the page


//string variables
var carName1 = "Volvo XC60";   			  // Using double quotes
var carName2 = 'Volvo XC60';   			  // Using single quotes
var answer1 = "It's alright";             // Single quote inside double quotes
var answer2 = "He is called 'Johnny'";    // Single quotes inside double quotes
var answer3 = 'He is called "Johnny"';    // Double quotes inside single quotes

//use escape characters
var x = "We are the so-called \"Vikings\" from the north."; 
var x = 'It\'s alright.';
var x = "The character \\ is called backslash.";

document.getElementById("demo").innerHTML = "Hello \
Dolly!";

document.getElementById("demo").innerHTML = "Hello " +
"Dolly!";

document.getElementById("demo").innerHTML = \
"Hello Dolly!";

//x==y will be true but x===y will be false as same values but different types
var x = "John";   
var y = new String("John"); // string objects


//to know the length of the string
str="Helloworld";

//length property
var sln = str.length;

//get starting indexof the given word in a string else returns -1
var pos = str.indexOf("locate");

//get lastindexof the given word in a string else returns -1
var pos = str.lastIndexOf("locate");

//to start search from starting position
var pos = str.indexOf("locate", 15);

//to start search from the end position
var pos = str.lastIndexOf("locate", 15);

//search substring in a string
var pos = str.search("locate");

// The search() method cannot take a second start position argument.
// The indexOf() method cannot take powerful search values (regular expressions).

//slice the string starting from 7th and ends at 12th positions
var res = str.slice(7, 13);

//slice the string starting from -12th and ends at -5th positions
var res = str.slice(-12, -6);

//starts slicing from 7th position and ends when string ends
var res = str.slice(7);

//starts slicing from -12th position and ends when string ends
var res = str.slice(-12);

//get substring from 7th to 12th but it cant accept negative values
var res = str.substring(7, 13);


//here 1st parameter is starting position and 2nd parameter is length of substring to cut
var res = str.substr(7, 6);


//substring cuts from -4th position to complete end
var res = str.substr(-4);

//replace the substring in a string
var n = str.replace("Microsoft", "W3Schools");

//it will not work if string contains lowercase words
var n = str.replace("MICROSOFT", "W3Schools");	//dont work

//it will now work if string contains lowercase words
var n = str.replace(/MICROSOFT/i, "W3Schools");	//i for insensitive

//replace all words with the same name
var n = str.replace(/Microsoft/g, "W3Schools");	//g for global

//change into uppercase
var text2 = text1.toUpperCase();  

//change into lowercase
var text2 = text1.toLowerCase();  

//to concatenate
var text3 = text1.concat(" ", text2);

//to concatenate
var text = "Hello".concat(" ", "World!");

//trim to remove space in the string
var str = "       Hello World!        ";
str.trim();

//to add at the starting
let str = "5";
str = str.padStart(4,0);
// result is 0005

//to add at the ending
let str = "5";
str = str.padEnd(4,0);
// result is 5000

//return character,character code of string characters at given location
var str = "HELLO WORLD";
str.charAt(0);        //return character 
str.charCodeAt(0);    //return character code
str[0] = "A";         //gives no error,but does not work

//convert string into array
var txt = "a,b,c,d,e";   // String
txt.split(",");          // Split on commas
txt.split(" ");          // Split on spaces
txt.split("|");          // Split on pipe
txt.split("");           // Split in characters
















