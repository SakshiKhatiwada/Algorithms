//Program to generate Random Numbers using Linear Congruential Method (Simulation and Modelling)

//Formula: X_i+1 = (a * X_i + c) mod m, where i = 0,1,2,...
// X_0 = seed, a = constant multiplier, c = increment, m = modulus or size

let randomNumbersArray = [];
let rand0to1 = [];

const linearCongruentialMethod = (a, c, m, X0, totalNumbers) => {
  randomNumbersArray.push(X0); //first element is seed
  rand0to1.push(X0 / 100);

  let val;
  for (let i = 0; i < totalNumbers; i++) {
    val = (a * randomNumbersArray[i] + c) % m;
    randomNumbersArray.push(val);
    rand0to1.push(val / 100);
    // console.log((a * X0 + c) % m);
  }
  console.log(randomNumbersArray);
  console.log(rand0to1);
};

linearCongruentialMethod(18, 43, 90, 27, 50);
