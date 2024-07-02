<h2><a href="https://leetcode.com/problems/majority-element">169. Majority Element</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

<h1> Solution </h1>
<p>To solve the Majority Element problem in linear time and <code>O(1)</code> space, we can use the Boyer-Moore Voting Algorithm. This algorithm works by maintaining a candidate for the majority element and a counter. The candidate is initialized to None, and the counter is initialized to 0. We then iterate through the array, updating the candidate and the counter based on the current element.</p>

<ul><h1>Explanation</h1>
	<li><h3>Initialization:</h3>We start with the candidate set to None and count set to 0.</li>
	<li><h3>First Pass (Finding the Candidate):</h3>We iterate through the array.
If the count is 0, we update the candidate to the current number and set the count to 1.
If the current number is the same as the candidate, we increment the count.
Otherwise, we decrease the count.</li>
	<li><h3>Returning the Candidate:</h3>The candidate at the end of the first pass is the majority element because the problem guarantees its existence.</li>
	
</ul>
<h1>This implementation ensures O(n) time complexity and O(1) space complexity.</h1>
