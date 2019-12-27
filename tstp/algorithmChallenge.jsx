//We'll pass you an array of two numbers. Return the sum of those two numbers plus the sum of all the numbers between them. The lowest number will not always come first.
//For example, sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both inclusive) is 10.

function sumAll(arr) {
  arr.sort((a,b) => a - b)
  let start = arr[0]
  let sum = 0;
    while (start < arr[1]+1) {
    sum+=start;
    start++;
  }
  return sum;
}

sumAll([1, 4]);


//Intermediate Algorithm Scripting: Diff Two ArraysPassed
//Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. In other words, return the symmetric difference of the two arrays.


function diffArray(arr1, arr2) {
    var newArr = [];
    // Same, same; but different.
    //compare every array to each other
    let newArr1 = arr1.filter(x => arr2.indexOf(x) === -1);
    let newArr2 = arr2.filter(x => arr1.indexOf(x) === -1)
    //push the new Arrays filtered into the final Array
    newArr1.forEach(x => newArr.push(x))
    newArr2.forEach(x => newArr.push(x))
    console.log(newArr);
    return newArr;
  }
  
  diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
  
  //Intermediate Algorithm Scripting: Seek and DestroyPassed
//You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

  function destroyer(arr) {
  // Remove all the values
  //extract first argument and make it an iterable array
  let newArr = [...arguments[0]]
  //dig through arguments and remove them from the newArray 
  for (let i = 1; i < arguments.length; i++) {
    let compareArgument = []
    compareArgument.push(arguments[i])
    newArr = newArr.filter(x => compareArgument.indexOf(x) === -1) 
  }
  return newArr;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3);

//Make a function that looks through an array of objects (first argument) and returns an array of all objects that have matching name and value pairs (second argument). 
//Each name and value pair of the source object has to be present in the object from the collection if it is to be included in the returned array.

function whatIsInAName(collection, source) {
  // What's in a name?
  var arr = [];
  // Only change code below this line
  //Trasnform source in the key value to check for. If all the values are in the 
  //collection object, then check if the value is the same. 
  var compare = Object.keys(source)
  var result = compare.map(x => source[x])
  //create value to store filtered array as hit keeps looping through
  let startAgain;
  //filter the array finding only the same value
  //first clean of array
  arr = collection.filter(x => x[compare[0]] === result[0])
  if (compare === 1) {
    return arr;
  }
  for (let key in compare) {
    arr = arr.filter(x => x[compare[key]] === result[key])
    startAgain = arr;
  }
  // Only change code above this line
  return arr;
}

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });
