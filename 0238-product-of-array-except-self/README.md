<h2><a href="https://leetcode.com/problems/product-of-array-except-self">238. Product of Array Except Self</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>
<h1>Explanation</h1>
<p>
	
<ul>
	<li><b>Initialization:</b> Create an answer array initialized with ones. This array will eventually hold the product of all elements except itself.</li>
	<li><b>Prefix Products:</b> Iterate over the array from left to right. Store the product of all previous elements in the answer array for each element. Update the prefix product for the next 	 
         iteration.</li>
	<li><b>Suffix Products:</b> Iterate over the array from right to left. For each element, multiply the current value in the answer array (which holds the prefix product) by the suffix product. Update the suffix product for the next iteration.</li>
</ul>
</p>
<p>
	By combining the prefix and suffix products, each element in the answer array ends up being the product of all elements except itself.
	This solution ensures that the problem is solved in O(n) time complexity and uses O(1) extra space complexity (ignoring the output array).
</p>
