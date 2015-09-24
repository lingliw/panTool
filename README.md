### panTool
**panTool** can convert multi markdown file to docx at same time.

### Usage Sample:
* Put **absolute directory path** which contains files in **dir.txt**  
  `C:\Users\v-welian\Documents\GitHub\azure-content-mooncake-pr\articles`
* Put file names in **file.txt**  
```python
  virtual-machines-a8-a9-a10-a11-specs.md
  virtual-machines-about.md
  virtual-machines-app-frameworks.md
  virtual-machines-arm-deployment.md
  virtual-machines-azure-resource-manager-architecture.md
```
* Run the command `python padocTool.py`, then converted **docx** file will be in the same directory with original markdown file.  
* Error message will be printed to the console, you can find which file was converted failed by checking the file names under *Error files:* and see detail message above it. 
```python
  get directory **virtual-machines**  
  Change dir to *azure-content-mooncake-prrticles*  
  Change dir to *azure-content-mooncake-prrticles virtual-machines*  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 129, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 128, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 127, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 126, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 125, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 124, column 1)  
  pandoc: Duplicate link reference `[StartingPoint]' "source" (line 123, column 1)  
  pandoc: Cannot decode byte '\x96': Data.Text.Internal.Encoding.Fusion.streamUtf8: Invalid UTF-8 stream  
  pandoc: Cannot decode byte '\x96': Data.Text.Internal.Encoding.Fusion.streamUtf8: Invalid UTF-8 stream  
  
  **Error files:**  
  virtual-machines-install-symantec.md  
  virtual-machines-install-trend.md  
```
