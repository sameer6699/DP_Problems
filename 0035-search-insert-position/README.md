<h2><a href="https://leetcode.com/problems/search-insert-position">35. Search Insert Position</a></h2><h3>Easy</h3><hr><p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<h1> Solution </h1>
<p>To solve the problem of finding the insert position for a target value in a sorted array with <code> O(log n) </code> runtime complexity, we can use binary search.</p>
<ul>
<li><b>Class Definition:</b> <p>The Solution class contains the <code> searchInsert</code> method, which takes nums and targets as input parameters.</p></li>
<li><b>Binary Search Implementation:</b>
<p>Initialize left pointer at the start and right pointer at the end of the array.
<b>Use a while loop to perform binary search:</b>
<b>Calculate the middle index mid.</b>
If the value at mid equals the target, <code> return mid.</code>
If the value at mid is less than the target, move the left pointer to <code> mid + 1. </code>
If the value at mid is greater than the target, move the right pointer to <code> id - 1.</code>
If the loop exits without finding the target, <code>left</code> will be the insertion position.</p></li>
<li><b>Return Value:</b> <p> The method returns the index where the target is found or the index where it should be inserted to maintain sorted order.</p></li>
<li>This solution ensures an O(log n) time complexity by using binary search to efficiently find the target or the appropriate insert position in the sorted array</li>
</ul>
