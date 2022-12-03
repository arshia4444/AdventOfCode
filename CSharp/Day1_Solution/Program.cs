
// ====== PART 1 ======
IEnumerable<string> calories = File.ReadLines("../../../input.txt");
List<int> sumOfCalories = new List<int>();
List<int> temp = new List<int>();

foreach (string calorie in calories)
{
    if (calorie != String.Empty)
        temp.Add(int.Parse(calorie));
    else
    {
        sumOfCalories.Add(temp.Sum());
        temp.Clear();
    }
}

// ====== PART 2 ======
sumOfCalories.Sort();
var sumOfTop3Calories = sumOfCalories.TakeLast(3).ToList().Sum();

Console.WriteLine($"PART 1: {sumOfCalories.Max()}");
Console.WriteLine($"PART 2: {sumOfTop3Calories}");

