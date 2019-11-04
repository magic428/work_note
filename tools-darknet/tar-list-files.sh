#!/bash
for file in ./*.tar.gz
do
	if test -f $file 
	then
		echo $file
		tar -xvf $file
	fi
done
