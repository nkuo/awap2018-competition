from base_player import BasePlayer
import networkx as nx
import logging

class Player(BasePlayer):
    def verify_and_place_unit(self, node, amount):
        if (self.list_graph[node] is None):
            print("Error: Node does not exist in list_graph")
            return

        if (self.list_graph[node][1]['owner'] != self.player_num):
            print("Error: You do not own this node you are placing into")
            self.find_caller()
            return

        if (amount <= 0):
            return

        if (amount > self.max_units):
            print("Error: You are trying to place too many units")
            return

        super().place_unit(node, amount)
        return
    def verify_and_move_unit(self, start, end, amount):
        if (amount <= 0):
            return

        start_node = self.list_graph[start]
        end_node = self.list_graph[end]

        if ((start is None) or (end is None)):
            print("Error: Node does not exist in list_graph")
            return

        if (start_node[1]['owner'] != self.player_num):
            print("Error: You do not own this node you are starting from")
            return

        if (start == end):
            return

        if (start_node[1]['old_units'] <= amount):
            print("Error: You do not have enough units to execute this movement")
            print("You are requesting", amount, "units, but you only have ", start_node[1]['old_units'], 'units')
            self.find_caller()
            return

        super().move_unit(start, end, amount)
        return

    """    
    self.dict_moves = {'place': [], 'move': []} # Action dictionary (you should only use our interface to modify this)
    self.player_num = p_id      # each player on a board will have a unique player number
    self.max_units = 0          # max number of units the player can place (updated after calling a place command)
    self.nodes = None           # list of nodes that this player owns (updated every turn)
    self.board = None           # networkx object (updated every turn)
    self.list_graph = None      # list representation of the entire board (updated every turn)
    """

    def __init__(self, p_id):
        super().__init__(p_id)  #Initializes the super class. Do not modify!
        self.phase = 0
        self.turnNum = 0
        logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        return


    # Called at the start of every placement phase and movement phase.

    def init_turn(self, board, nodes, max_units):
        super().init_turn(board, nodes, max_units)       #Initializes turn-level state variables
        self.turnNum += 1
        if (self.turnNum == 21):
            self.phase = 1
        logging.debug(self.nodes)
        return


    # Called during the placement phase to request player moves
    def player_place_units(self):

        return self.dict_moves #Returns moves built up over the phase. Do not modify!


    # Called during the move phase to request player moves
    def player_move_units(self):
        return self.dict_moves #Returns moves built up over the phase. Do not modify!
