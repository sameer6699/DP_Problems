<h2><a href="https://leetcode.com/problems/create-a-dataframe-from-list">3062. Create a DataFrame from List</a></h2><h3>Easy</h3><hr><p>Write a solution to <strong>create</strong> a DataFrame from a 2D list called <code>student_data</code>. This 2D list contains the IDs and ages of some students.</p>

<p>The DataFrame should have two columns, <code>student_id</code> and <code>age</code>, and be in the same order as the original 2D list.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:
</strong>student_data:<strong>
</strong><code>[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]</code>
<strong>Output:</strong>
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
<strong>Explanation:</strong>
A DataFrame was created on top of student_data, with two columns named <code>student_id</code> and <code>age</code>.
</pre>
<h1>Explanation</h1>
<p>This code defines the function <code>createDataframe</code> which takes student_data, a list of lists of integers, and returns a pandas DataFrame with columns <code>student_id</code> and <code>age.</code> The driver code at the end demonstrates how to call this function and print the resulting DataFrame.</p>
