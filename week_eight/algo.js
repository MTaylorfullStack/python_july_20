// is palindrome
// accepting a string, return true if the string is a palindrome
// otherwise, return false

// declare our function, accepting a string
// for loop, loop through string
    // if first value is not same as last value
        // return false
// return true

function palindrome(pal){
    console.log("Testing string for palindrome")
    for(let i=0; i<pal.length/2; i++){
        if (pal[i] !== pal[pal.length-1-i]){
            return false
        }
    }
    return true
}

console.log(palindrome("banana"));

// word = "banana"

// if (word[0] !== word[word.length-1-0]){       
//     result = word.substring(0)
// }

// console.log(word.substring(1), "this is what substring does to banana")

// declare our function, accepting a string
// call palindrome, pass in string
// if result is true
    // return string
// else
    // call palindrome with modified string string.substring(1)

// longest palindrome that is a word
// recursive approach

function longestPalindromeRecurs(pal){
    // console.log(pal.split(' '))
    if (palindrome(pal)){
        console.log("Finally have my palindrome")
        return pal
    } else {
        console.log("Still not a palindrome, making recursive call")
        console.log(pal.substring(1))
        return longestPalindromeRecurs(pal.substring(1))
    }
}

console.log(longestPalindromeRecurs("Hello world! I am dealing with recursion"))

function longestPalindrome(pal){
    pal_arr = pal.split(' ');
    completed_palindromes = {}
    for(let i=0; i<pal_arr.length; i++){
        if(palindrome(pal_arr[i])){
            completed_palindromes[pal_arr[i]] = pal_arr[i].length
        }
    }
    var max = 0;
    var longest_pal = "";
    for (single_pal in completed_palindromes){
        if(completed_palindromes[single_pal] > max){
            max = completed_palindromes[single_pal]
            longest_pal = single_pal
        }
    }
    console.log(completed_palindromes)
    return longest_pal
}

console.log(longestPalindrome("tacocat racecar mom dad jjjjjjjjjj"))


// mode of array
// given an array, return the mode
// mode == value that appears most frequently in the data set

function modeOfArray(arr){
    // find most common value in arr
    // keep track of count
    var potential_modes = {}
    for(let i = 0; i < arr.length; i++){
        // creating a key in potential_modes object
        if (arr[i] in potential_modes){
            potential_modes[arr[i]] += 1
        } else {
            potential_modes[arr[i]] = 1
        }
    }
    // defining max as first value in object
    var max = potential_modes[arr[0]];
    var mode = arr[0];
    for (key in potential_modes){
        // if we find value greater than max
        if(max<potential_modes[key]){
            // change max
            max = potential_modes[key]
            mode = key
        }
    }
    return mode
}

console.log(modeOfArray(['hi', 'hello', 'hi', 'hello', 'hello', 3, 3, 3, 3, 3, 3, 3, 3, 3]))