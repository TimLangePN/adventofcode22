var list = File.ReadAllLines(@"C:\Users\tim.lange\Documents\Git\adventofcode22\day3\list.txt");

List<int> points = new List<int>();

foreach (string line in list)
{
    points.Add(CompareCharacters(line));
}

static int CompareCharacters(string line)
{
    var first = line.Substring(0, line.Length / 2);
    var second = line.Replace(first, "");

    foreach (char letter in first)
    {
        if (second.Contains(letter))
        {
            int Score = GetScore(letter);
            return Score;
        }
    };
    return 0;
}

static int GetScore(char letter)
{
    if (char.IsUpper(letter) == true)
    {
        return(int)letter - 38;
    }
    else
    {
        return (int)letter - 96;
    }
}

Console.WriteLine(points.Sum(x => Convert.ToInt32(x)));