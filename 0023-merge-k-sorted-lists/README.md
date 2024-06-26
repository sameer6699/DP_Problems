<h2><a href="https://leetcode.com/problems/merge-k-sorted-lists">23. Merge k Sorted Lists</a></h2><h3>Hard</h3><hr><p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked lists into one sorted linked list and return it.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
</ul>

<h1> Solution for the Given Problem </h1>
<p> To merge k sorted linked lists into one sorted linked list, we can use a min-heap (priority queue) to efficiently get the smallest node among the heads of the lists. This approach helps in maintaining the overall time complexity to 
𝑂(𝑁log𝑘) O(Nlogk), where 𝑁 N is the total number of nodes and  𝑘 k is the number of linked lists. </p>

<ul>
	<li>Explanation</li>
	<li><code>List Node Class:</code>Defines the structure of a node in the linked list.</li>
	<li>mergeKLists Method:</li>
	<li>Uses a min-heap to keep track of the smallest node among the heads of the lists.
	Initializes the heap with the head of each list.
	Extracts the smallest node from the heap, add it to the result list, and pushes the next node from the same list into the heap.
	It continues until the heap is empty.</li>
</ul>
