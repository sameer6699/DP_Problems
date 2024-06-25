<h2><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array">34. Find First and Last Position of Element in Sorted Array</a></h2><h3>Medium</h3><hr><p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

<h1>Solution</h1>
<p>To solve the problem of finding the first and last position of a target value in a sorted array with <code>O(log n)</code> runtime complexity, we can use binary search.</p>

<ul>
	<li><b>Class Definition:</b> <p>The <code> Solution</code> class contains the <code> searchRange</code> method, which takes nums and targets as input parameters.</p></li>
	<li><b>Helper Function:</b> <p>find_left: This function finds the leftmost <code>(first)</code> index of the target. It uses binary search to locate the first occurrence of the target by moving right when <code>nums[mid]</code> is greater than or equal to the target.
	find_right: This function finds the rightmost <code>(last)</code> index of the target. It uses binary search to locate the last occurrence of the target by moving left when <code>nums[mid]</code> is less than or equal to the target.</p></li>
	<li><b>Method Implementation:</b> <p>Calculate the <code>left</code> and <code>right</code> indices of the target using the helper functions.
	Check if the indices are valid and if the values at these indices match the target.
	Return the indices if valid; otherwise,<code> return [-1, -1].</code></p></li>
	<li>This approach ensures the algorithm runs in O(log n) time complexity, leveraging binary search to efficiently find the first and last positions of the target in the sorted array.</li>
</ul>
