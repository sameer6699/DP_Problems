<h2><a href="https://leetcode.com/problems/h-index">274. H-Index</a></h2><h3>Medium</h3><hr><p>Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their <code>i<sup>th</sup></code> paper, return <em>the researcher&#39;s h-index</em>.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank">definition of h-index on Wikipedia</a>: The h-index is defined as the maximum value of <code>h</code> such that the given researcher has published at least <code>h</code> papers that have each been cited at least <code>h</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> citations = [3,0,6,1,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> citations = [1,3,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == citations.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= citations[i] &lt;= 1000</code></li>
</ul>

<h1>Explnation:</h1>
<p>
	<ul>
		<li>sorting:
  			<ul>
				<li>Sort the citations array in descending order.</li>
			</ul>	
		</li>
		<li>Finding t H-Index: 
			<ul>
				<li>Iterate through the sorted list.</li>
				<li>For each citation value at index I, check if the citation is at least I + 1.</li>
    				<li>If it is, update h_index to i + 1.</li>
				<li>If it's not, break the loop since further elements will not satisfy the condition.</li>
			</ul>
		</li>
		<li>Return the H-Index:
			<ul>
				<li> Return the final value of h_index. </li>
			</ul>
		</li>
	</ul>
</p>
