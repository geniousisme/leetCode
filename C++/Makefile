# SRC_JAVA = $(shell find . -name *.java)
# SRC_CPP = $(shell find . -name *.cpp)
# SRC_C = $(shell find . -name *.c)

# TARGET_JAVA = $(SRC_JAVA:%.java=%.class)
# TARGET_OBJ = $(SRC_CPP:%.cpp=%.obj)
# TARGET_O = $(SRC_C:%.c=%.o)

# all: $(TARGET_JAVA) $(TARGET_O) $(TARGET_OBJ)

# %.class: %.java
# 	javac -classpath $(shell dirname $<) $<

# %.o: %.c
# 	gcc -c $< -o $@

# %.obj: %.cpp
# 	gcc -c $< -o $@

# clean:
# 	rm -f $(TARGET_JAVA)
# 	rm -f $(TARGET_O)
# 	rm -f $(TARGET_OBJ)

# todo:
# 	@ag -g "cpp|py|java" | sed -e 's/\/.*//' | sort | uniq -c | sort | ag "^\s*[12]"

# commited:
# 	@git ls-files --directory | grep "/" | sed "s/\/.*//" | sort | uniq
# 	@git ls-files --directory | grep "/" | sed "s/\/.*//" | sort | uniq | wc -l

# uncommit:
# 	@(ag -g "cpp|py|java" | sed -e 's/\/.*//' | sort | uniq; git ls-files --directory | grep "/" | sed "s/\/.*//" | sort | uniq) | sort | uniq -u
# 	@(ag -g "cpp|py|java" | sed -e 's/\/.*//' | sort | uniq; git ls-files --directory | grep "/" | sed "s/\/.*//" | sort | uniq) | sort | uniq -u | wc -l

# total:
# 	@ag -g "cpp|py|java" | sed -e 's/\/.*//' | sort | uniq | sort | uniq -u
# 	@ag -g "cpp|py|java" | sed -e 's/\/.*//' | sort | uniq | sort | uniq -u | wc -l

# CC and CFLAGS are varilables
CC=g++
CFLAGS = -c
AR = ar
ARFLAGS = rcv
# -c option ask g++ to compile the source files, but do not link.
# -g option is for debugging version
# -O2 option is for optimized version
DBGFLAGS = -g -D_DEBUG_ON_
OPTFLAGS = -O2

cpp_dir = C++
bin_dir = $(cpp_dir)/bin
out_dir = $(cpp_dir)/out

$(cpp_dir)/%.cpp: %.o Utils.o
		    	$(CC) $(OPTFLAGS) $(out_dir)/%.o $(out_dir)/Utils.o -o $(bin_dir)/%

%.o 		: $(cpp_dir)/%.cpp
				$(CC) $(CFLAGS) $(OPTFLAGS) $< -o $(out_dir)/$@

Utils.o		: $(cpp_dir)/include/utils/Utils.cpp 
				$(CC) $(CFLAGS) $(OPTFLAGS) $< -o $(out_dir)/Utils.o
			
# clean all the .o and executable files
clean		:
			    rm -rf $(out_dir)/*.o $(bin_dir)/*

run 		:
			  	./$(bin_dir)/%
		
# lib/libtm_usage.a: tm_usage.o
# 	$(AR) $(ARFLAGS) lib/libtm_usage.a tm_usage.o

# tm_usage.o: lib/tm_usage.cpp lib/tm_usage.h
# 	$(CC) $(CFLAGS) $<

# g++ -c -O2 C++/include/utils/Utils.cpp -o C++/bin/Utils.o 

# g++ -c -O2 C++/83-RemoveDuplicatesFromSortedList.cpp -o C++/bin/83.o
# g++ -O2 C++/bin/83.o C++/bin/Utils.o -o C++/bin/83
# ./C++/bin/83



