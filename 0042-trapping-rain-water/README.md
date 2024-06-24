<h2><a href="https://leetcode.com/problems/trapping-rain-water">42. Trapping Rain Water</a></h2><h3>Hard</h3><hr><p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" />
<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>
<h1> Solution </h1>
<p> To solve the "Trapping Rain Water" problem, we can use the two-pointer approach. This approach is efficient in terms of both time and space complexity. The idea is to use two pointers to traverse the height array from both ends towards the center and calculate the trapped water based on the minimum of the maximum heights encountered. </p>

<ul><h1><b>Explanation:</b></h1>
	<li>Initialization: <p> Use two pointers, left starting at the beginning and right at the end of the array.
	Maintain two variables, <code> left_max,</code> and <code>right_max,</code> to store the maximum heights encountered from the left and right, respectively.
	<br>Use a variable water to accumulate the total amount of trapped water.</p></li>
	<li>Two-Pointer Traversal:<p>While left is less than right, compare the heights at the left and right pointers.
	If the height at left is less than or equal to the height at right:
If <code>height[left]</code> is greater than or equal to <code>left_max,</code> update <code>left_max.</code>
Otherwise, calculate the trapped water at <code>left as left_max - height[left]</code> and add it to water.
Move the left pointer to the right.
If the height at the right is less than the height at the left:
If height[right] is greater than or equal to right_max, update right_max.
Otherwise, calculate the trapped water at right as right_max - height[right] and add it to water.
Move the right pointer to the left.</p></li>
</ul>

