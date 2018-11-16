
# coding: utf-8

# In[28]:


class Maze:
    def __init__(self, filename):
        """initialize the maze, start and exit point, and a robot at start point"""
        #initialize the private members
        self.__exit = []
        self.__start = []
        self.__maze = []
        #open the file
        with open(filename,"r") as fh:
            contents = fh.readlines()
            for i in range(len(contents)):
                contents[i] = contents[i].rstrip()
                self.__maze.append(contents[i])
                #find the exit
                if i == 0:
                    for j in range(len(contents[i])):
                        if contents[i][j] == "0":
                            if self.__exit != []:
                                raise Exception("More than one exits.")
                            self.__exit = [0,j]
                elif contents[i][0] == "0":
                    if self.__exit != []:
                                raise Exception("More than one exit.")
                    self.__exit = [i,0]
                elif contents[i][-1] == "0":
                    if self.__exit != []:
                                raise Exception("More than one exit.")
                    self.__exit = [i,len(contents[i])-1]
                elif i == len(contents)-1:
                    for j in range(len(contents[i])):
                        if contents[i][j] == "0":
                            if self.__exit != []:
                                raise Exception("More than one exit.")
                            self.__exit = [0,j]
                #find the start
                for j in range(len(contents[i])):
                    if contents[i][j] == "2":
                        if self.__start != []:
                            raise Exception("More than one start")
                        self.__start = [i,j]
                self.__robot = Robot(self,self.__start)
    @property
    def robot(self):
        return self.__robot
    def get_finish(self):
        return self.__exit
    def get_maze(self):
        return self.__maze
    def get_start(self):
        return self.__start
    
class Robot:
    def __init__(self,maze,start):
        self.__cur_pos = start
        self.__last_pos = self.__cur_pos
        self.__last_dir = ""
        self.__maze = maze
        
    def change_pos(self,pos):
        self.__last_pos = self.__cur_pos
        self.__cur_pos = pos
        
    def change_dir(self,direction):
        self.__last_dir = direction
        
    def walk_options(self):
        x = self.__cur_pos[0]
        y = self.__cur_pos[1]
        opt = {"left":[0,0],"right":[0,0],"up":[0,0],"down":[0,0]}
        maze_map = self.__maze.get_maze()
        if maze_map[x-1][y] != "1":
            opt["up"]=[x-1,y]
        else:
            del opt["up"]
        if maze_map[x][y-1]:
            opt["left"]=[x,y-1]
        else:
            del opt["left"]
        if maze_map[x+1][y]:
            opt["down"]=[x+1,y]
        else:
            del opt["down"]
        if maze_map[x][y+1]:
            opt["right"]=[x,y+1]
        else:
            del opt["right"]
        return opt
    
    def is_finished(self):
        if self.__cur_pos == self.__maze.get_finish():
            return True
        return False


# In[ ]:


#algorithms

