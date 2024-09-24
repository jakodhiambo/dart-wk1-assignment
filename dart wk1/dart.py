void main() {
  // Part 1: Define Variables
  int myInt = 42;
  double myDouble = 3.14;
  String myString = "Hello, Dart!";
  bool myBool = true;
  List<int> myList = [1, 2, 3, 4, 5];

  // Print the initialized variables
  print('Integer: $myInt');
  print('Double: $myDouble');
  print('String: $myString');
  print('Boolean: $myBool');
  print('List: $myList');

  // Part 2: Type Conversion Functions
  int stringToInt(String str) {
    return int.parse(str);
  }

  double stringToDouble(String str) {
    return double.parse(str);
  }

  String intToString(int num) {
    return num.toString();
  }

  double intToDouble(int num) {
    return num.toDouble();
  }

  // Function for Conversion
  void convertAndDisplay(String numberStr) {
    int intValue = stringToInt(numberStr);
    double doubleValue = stringToDouble(numberStr);
    print('Converted String to Int: $intValue');
    print('Converted String to Double: $doubleValue');
  }

  // Test the convertAndDisplay function
  convertAndDisplay("100");

  // Part 3: Control Flow with If-Else Statements
  int numberToCheck = -5; // Example number

  if (numberToCheck > 0) {
    print('The number is positive.');
  } else if (numberToCheck < 0) {
    print('The number is negative.');
  } else {
    print('The number is zero.');
  }

  // Checking eligibility to vote
  int age = 20; // Example age
  if (age >= 18) {
    print('Eligible to vote.');
  } else {
    print('Not eligible to vote.');
  }

  // Part 4: Switch Case Example
  int day = 3; // Example day (1 for Monday, etc.)
  switch (day) {
    case 1:
      print('Monday');
      break;
    case 2:
      print('Tuesday');
      break;
    case 3:
      print('Wednesday');
      break;
    case 4:
      print('Thursday');
      break;
    case 5:
      print('Friday');
      break;
    case 6:
      print('Saturday');
      break;
    case 7:
      print('Sunday');
      break;
    default:
      print('Invalid day');
  }

  // Part 5: Loops
  // For loop
  print('For loop from 1 to 10:');
  for (int i = 1; i <= 10; i++) {
    print(i);
  }

  // While loop
  print('While loop from 10 to 1:');
  int j = 10;
  while (j >= 1) {
    print(j);
    j--;
  }

  // Do-while loop
  print('Do-while loop from 1 to 5:');
  int k = 1;
  do {
    print(k);
    k++;
  } while (k <= 5);

  // Part 6: Combining Data Types and Control Flow
  List<int> numbers = [3, 8, 15, 22, 37, 50, 101];

  print('Processing numbers:');
  for (int num in numbers) {
    print(num);
    // Check if the number is even or odd
    if (num % 2 == 0) {
      print('$num is even.');
    } else {
      print('$num is odd.');
    }

    // Categorize the number using switch statement
    switch (num) {
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
      case 6:
      case 7:
      case 8:
      case 9:
      case 10:
        print('$num is small.');
        break;
      case 11:
      case 12:
      case 13:
      case 14:
      case 15:
      case 16:
      case 17:
      case 18:
      case 19:
      case 20:
      case 21:
      case 22:
      case 23:
      case 24:
      case 25:
      case 26:
      case 27:
      case 28:
      case 29:
      case 30:
      case 31:
      case 32:
      case 33:
      case 34:
      case 35:
      case 36:
      case 37:
      case 38:
      case 39:
      case 40:
      case 41:
      case 42:
      case 43:
      case 44:
      case 45:
      case 46:
      case 47:
      case 48:
      case 49:
      case 50:
      case 51:
      case 52:
      case 53:
      case 54:
      case 55:
      case 56:
      case 57:
      case 58:
      case 59:
      case 60:
      case 61:
      case 62:
      case 63:
      case 64:
      case 65:
      case 66:
      case 67:
      case 68:
      case 69:
      case 70:
      case 71:
      case 72:
      case 73:
      case 74:
      case 75:
      case 76:
      case 77:
      case 78:
      case 79:
      case 80:
      case 81:
      case 82:
      case 83:
      case 84:
      case 85:
      case 86:
      case 87:
      case 88:
      case 89:
      case 90:
      case 91:
      case 92:
      case 93:
      case 94:
      case 95:
      case 96:
      case 97:
      case 98:
      case 99:
      case 100:
        print('$num is medium.');
        break;
      default:
        print('$num is large.');
    }
  }
}