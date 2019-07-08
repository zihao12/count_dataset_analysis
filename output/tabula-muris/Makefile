all: droplet FACS

droplet: 10x.zip
	unzip -q 10x.zip
	unzip -q droplet.zip
	rm -r __MACOSX/
	chmod -R o-w droplet/

FACS: facs-sorted-smart-seq2.zip
	unzip -q facs-sorted-smart-seq2.zip
	unzip -q FACS.zip
	rm -r __MACOSX/
	chmod -R o-w FACS/

facs-sorted-smart-seq2.zip:
	curl "https://ndownloader.figshare.com/articles/5829687/versions/8" -o $@

10x.zip:
	curl "https://ndownloader.figshare.com/articles/5968960/versions/3" -o $@
