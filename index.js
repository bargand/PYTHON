// Function to calculate the number of correct and wrong answers
function calculateAnswers(totalMarks, marksPerQuestion, penaltyPerWrongAnswer, totalQuestions) {
    // Calculate the maximum possible score
    const maxPossibleScore = totalQuestions * marksPerQuestion;
  
    // Calculate the number of correct answers
    const correctAnswers = Math.floor((totalMarks - maxPossibleScore) / penaltyPerWrongAnswer);
  
    // Calculate the number of wrong answers
    const wrongAnswers = totalQuestions - correctAnswers;
  
    return { correctAnswers, wrongAnswers };
  }
  
  // Main function
  function main() {
    // Define constants
    const totalMarks = 41;
    const marksPerQuestion = 3;
    const penaltyPerWrongAnswer = -1;
    const totalQuestions = 25;
  
    // Calculate answers
    const { correctAnswers, wrongAnswers } = calculateAnswers(
      totalMarks,
      marksPerQuestion,
      penaltyPerWrongAnswer,
      totalQuestions
    );
  
    // Display results
    console.log("Number of correct answers:", correctAnswers);
    console.log("Number of wrong answers:", wrongAnswers);
  }
  
  // Call the main function
  main();
  