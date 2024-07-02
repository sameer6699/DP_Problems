<h2><a href="https://leetcode.com/problems/rotate-array">189. Rotate Array</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, rotate the array to the right by <code>k</code> steps, where <code>k</code> is non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7], k = 3
<strong>Output:</strong> [5,6,7,1,2,3,4]
<strong>Explanation:</strong>
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-100,3,99], k = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Try to come up with as many solutions as you can. There are at least <strong>three</strong> different ways to solve this problem.</li>
	<li>Could you do it in-place with <code>O(1)</code> extra space?</li>
</ul>
<h1> Solution </h1>
<p>To solve the problem of rotating an array to the right by k steps in place with O(1) extra space, we can use the reverse method. This involves reversing parts of the array and then reversing the entire array. Here's how you can implement it:</p>
<ol>
	<li>Reverse the entire array.</li>
	<li>Reverse the first k elements.</li>
	<li>Reverse the remaining <code>n - k</code>elements.</li>
</ol>
<h3>Explanation</h3>
<ul>
	<li><h3>Reverse the Entire Array:</h3>This makes the last k elements become the first k elements but in reverse order, and the first n-k elements become the last n-k elements but in reverse order.</li>
 	<li><h3>Reverse the First k Elements:</h3>This restores the original order of the first k elements which are now in their final rotated positions.</li>
  	<li><h3>Reverse the Remaining n-k Elements:</h3>This restores the original order of the remaining elements.</li>
	
</ul>
<h2>By following these steps, the array is rotated in place with O(1) extra space.</h2>
