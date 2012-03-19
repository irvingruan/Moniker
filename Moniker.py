#!/usr/bin/env python

# Author: Irving Ruan
# Contact: irvingruan@gmail.com

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import getopt

def usage():
	sys.stderr.write("Usage: ./Moniker.py -p [path] -c [case]\n")
	sys.stderr.write("Type `./Moniker.py --help` for more info\n")
	
def help():
	sys.stderr.write("Flags of Moniker are:\n")
	sys.stderr.write(" -p [path] The directory path to search for unformatted directories\n")
	sys.stderr.write(" -c [case: Upper | Lower] Flag to set upper or lowercase formatting for directories\n\n")
	sys.stderr.write("Example: ./Moniker.py -p ~/Documents/ -c Upper\n")
	sys.stderr.write("e.g. Find all directories in ~/Documents and change them to proper uppercase for the first letter\n")

def rename_directories(path, case):
	directories = os.listdir(os.path.abspath(os.path.expanduser(path)))
	
	changedLowerFlag = 0
	changedUpperFlag = 0
	filesChanged = 0
	
	# We're impartial to files vs directories. Rename both for consistency's    sake
	for item in directories:
		if case.lower() == "upper": 
			if item[0].isupper():
				pass
			else:
				changedUpperFlag = 1
				os.rename(os.path.join(path, item), os.path.join(path, item[0].upper() + item[1:]))
				newName = item[0].upper() + item[1:]
				sys.stdout.write("Renamed `" + item + "` to `" + newName + "`\n")
				filesChanged += 1		
		elif case.lower() == "lower":
			if item[0].islower():
				pass
			else:
				changedLowerFlag = 1
				os.rename(os.path.join(path, item), os.path.join(path, item[0].lower() + item[1:]))
				newName = item[0].lower() + item[1:]
				sys.stdout.write("Renamed `" + item + "` to `" + newName + "`\n")
				filesChanged += 1
				
	if filesChanged == 0:
		sys.stdout.write("No changes made. All files and directories are already properly " + case + "-cased.\n")
	else:
		sys.stdout.write("\nTotal number of files/directories renamed: " + str(filesChanged) + "\n")
				

def main():
	if len(sys.argv) != 5:	
		if len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "--h"):
			help()
			return False
		else:
			usage()
			return False
			
	path = sys.argv[2]
	case = sys.argv[4]
	
	# Check validity of path provided
	if not(os.path.isdir(path)):
		sys.stderr.write("Error: '" + path + "' is an invalid path\n")
		usage()
		return False
		
	# Make sure the case flag is valid
	if case.lower() != "upper" and case.lower() != "lower":
		sys.stderr.write("Error: '" + case + "' is an invalid case flag\n")
		usage()
		return False
		
	rename_directories(path, case)	
		
if __name__ == "__main__":
	main()