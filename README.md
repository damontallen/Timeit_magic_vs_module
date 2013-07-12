Timeit_magic_vs_module
======================

This is a comparison between the IPython %timeit magic command and the Python timeit module with an HTML table library for the results.

The motivation of this project was the slight frustration that I couldn't get a numerical value from IPython's %timeit magic.
After looking into the timeit module in Python and seeing [this notebook's](http://nbviewer.ipython.org/837630cc64bc258a2a7a) use of decorators
I was determined to make a library that would make an HTML table of the results.

<html>
<table border="1" cellpadding="3" cellspacing="0"  style="border:1px solid black;border-collapse:collapse;">
<tr><td>Function</td><td>Best time of 3</td><td>Loops</td></tr>
        <tr><td>add</td><td>519.643 us</td><td>1000</td></tr>
        <tr><td>mult</td><td>520.225 us</td><td>1000</td></tr>
        <tr><td>dist</td><td>670.213 us</td><td>1000</td></tr>
       </table>
</html>

The notebook is displayed [here](http://nbviewer.ipython.org/urls/github.com/damontallen/Timeit_magic_vs_module/raw/master/timeit_magic_vs_timeit_module.ipynb).
