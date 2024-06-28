<h2><a href="https://leetcode.com/problems/daily-temperatures">739. Daily Temperatures</a></h2><h3>Medium</h3><hr><p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li>
</ul>

<h1>Solution</h1>
<p>To solve the "Daily Temperatures" problem, we can use a stack to keep track of the indices of the temperatures. The idea is to maintain a decreasing stack such that whenever we encounter a warmer temperature, we can pop from the stack and calculate the difference in days.</p>
<p>
<h1>Explanation:</h1>
<ul>
	<li><b><h3>Initialization:</h3></b>We initialize an array answer of the same length as temperatures with all elements set to 0.
	We use a stack to keep track of the indices of the temperatures in a decreasing order. </li>
	<li><b><h3>Iterate through the temperatures:</h3></b>For each temperature at index I, we check if it is warmer than the temperature at the index stored at the top of the stack.
	If it is, we pop the index from the stack and calculate the difference between the current index I and the popped index to get the number of days until a warmer temperature.
	We continue this process until the stack is empty or the current temperature is not warmer than the temperature at the top of the stack.
	Finally, we push the current index i onto the stack.</li>
	<li><b><h3>Return the result:</h3></b>After processing all the temperatures, the answer array will contain the number of days to wait for a warmer temperature for each day.</li>
	<p>This approach ensures that each temperature is processed in constant time on average, making the solution efficient with a time complexity of <code>O(n).</code></p>
</ul>	
</p>
