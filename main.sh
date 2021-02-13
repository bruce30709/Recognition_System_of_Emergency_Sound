while :
do
if [ -e /mnt/hgfs/kkk/ass.txt ]
then
python a.py | grep "jj \[" | sed 's/\[//' | sed 's/\.\]//' | awk '{ print $2 }'  | tee /mnt/hgfs/detect/flag.txt | awk '{if($1>=80){print "success"}}'
fi
done
