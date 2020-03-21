class Pieces:
    """Represents the Pieces on the board."""

    def __init__(self):
        self._red_palace = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]  # Initializes red palace positions.
        self._black_palace = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]
        # Initializes black palace positions.
        self._red_zone = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1",
                          "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2",
                          "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3",
                          "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4",
                          "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"]
        # Initializes red players side of the river.
        self._black_zone = ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6",
                            "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7",
                            "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8",
                            "a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9",
                            "a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10"]
        # Initializes black players side of the river.
        self._board = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1",
                       "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2",
                       "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3",
                       "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4",
                       "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5",
                       "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6",
                       "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7",
                       "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8",
                       "a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9",
                       "a10", "b10", "c10", "d10", "e10", "f10", "g10", "h10", "i10"]
        # Initializes board positions in list form minus the pieces for reference.

    def identify_piece(self, move_from, move_to):
        """Function to identify which piece is being called upon."""
        if self._game_board[move_from] == "":  # Checks if position being called contains a piece.
            return False
        elif "red" in self._game_board[move_from] and self._move_counter % 2 == 0:
            # Checks if piece in called position is red and if it is blacks turn.
            return False
        elif "red" in self._game_board[move_from] and self._move_counter % 2 != 0:
            # Checks if piece in called position is red and if it is reds turn.
            if "red general" in self._game_board[move_from]:  # Checks if piece is red's general.
                return self.move_red_general(move_from, move_to)  # Iterates through red general function.
            elif "red guard" in self._game_board[move_from]:  # Checks if piece is red's guard.
                return self.move_red_guard(move_from, move_to)  # Iterates through red guard function.
            elif "red elephant" in self._game_board[move_from]:  # Checks if piece is red's elephant.
                return self.move_red_elephant(move_from, move_to)  # Iterates through red elephant function.
            elif "red horse" in self._game_board[move_from]:
                # Checks if piece is red's horse.
                return self.move_red_horse(move_from, move_to)  # Iterates through red horse function.
            elif "red chariot" in self._game_board[move_from]:
                # Checks if piece is red's chariot.
                return self.move_red_chariot(move_from, move_to)  # Iterates through red chariot function.
            elif "red cannon" in self._game_board[move_from]:
                # Checks if piece is red's cannon.
                return self.move_red_cannon(move_from, move_to)  # Iterates through red cannon function.
            elif "red soldier" in self._game_board[move_from]:  # Checks if piece is red's soldier.
                return self.move_red_soldier(move_from, move_to)  # Iterates through red soldier function.
        elif "black" in self._game_board[move_from] and self._move_counter % 2 == 0:
            # Checks if position contains black piece and is black players turn.
            if "black general" in self._game_board[move_from]:  # Checks if piece is black's general.
                return self.move_black_general(move_from, move_to)  # Iterates through black general function.
            elif "black guard" in self._game_board[move_from]:  # Checks if piece is black's guard.
                return self.move_black_guard(move_from, move_to)  # Iterates through black guard function.
            elif "black elephant" in self._game_board[move_from]:  # Checks if piece is black's elephant.
                return self.move_black_elephant(move_from, move_to)  # Iterates through black elephant function.
            elif "black horse" in self._game_board[move_from]:  # Checks if piece is black's horse.
                return self.move_black_horse(move_from, move_to)  # Iterates through black horse function.
            elif "black chariot" in self._game_board[move_from]:  # Checks if piece is black's chariot.
                return self.move_black_chariot(move_from, move_to)  # Iterates through black chariot function.
            elif "black cannon" in self._game_board[move_from]:  # Checks if piece is black's cannon.
                return self.move_black_cannon(move_from, move_to)  # Iterates through black cannon function.
            elif "black soldier" in self._game_board[move_from]:  # Checks if piece is black's soldier.
                return self.move_black_soldier(move_from, move_to)  # Iterates through black soldier function.
        elif "black" in self._game_board[move_from] and self._move_counter % 2 != 0:
            # Checks if position contains black piece and if it is red players turn.
            return False

    def move_red_general(self, move_from, move_to):
        """Function to move red player's general"""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif move_to not in self._red_palace:  # Checks if desired position is within red player's palace.
            return False
        elif self._board.index(move_from) + 9 == self._board.index(move_to):
            #  Checks if desired position is one position vertically down of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_from] = "red general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 9 == self._board.index(move_to):
            # Checks if desired position is one position vertically up from current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_from] = "red general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) + 1 == self._board.index(move_to):
            # Checks if desired position is one position to the right of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_from] = "red general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 1 == self._board.index(move_to):
            # Checks if desired position is one position to the left of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_from] = "red general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        else:
            return False

    def move_red_guard(self, move_from, move_to):
        """Function to move red player's guard."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is occupied by another red piece.
            return False
        elif move_to not in self._red_palace:  # Checks if desired position is in red's palace.
            return False
        elif self._board.index(move_from) + 10 == self._board.index(move_to):
            # Checks if desired position is down a row diagonally to the right.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "red guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 10 == self._board.index(move_to):
            # Checks if desired position is up one row diagonally to the left.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "red guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) + 8 == self._board.index(move_to):
            # Checks if desired position is down one row diagonally to the left.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "red guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 8 == self._board.index(move_to):
            # Checks if desired position is up on row diagonally to the right.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "red"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "red guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        else:
            return False

    def move_red_elephant(self, move_from, move_to):
        """Function to move red player's elephant."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif move_to in self._black_zone:  # Check if desired location is across the river.
            return False
        elif self._board.index(move_from) + 16 == self._board.index(move_to):
            # Checks if desired position is down two rows diagonally to the left.
            temp = self._board[self._board.index(move_from) + 8]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 16 == self._board.index(move_to):
            # Checks if desired position is up two rows diagonally to the right.
            temp = self._board[self._board.index(move_from) - 8]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 20 == self._board.index(move_to):
            # Checks if desired position is down two rows diagonally to the right.
            temp = self._board[self._board.index(move_from) + 10]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 20 == self._board.index(move_to):
            # Checks if desired position is up two rows diagonally to the left.
            temp = self._board[self._board.index(move_from) - 10]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        else:
            return False

    def move_red_horse(self, move_from, move_to):
        """Function to move red player's horse."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif self._board.index(move_from) + 17 == self._board.index(move_to):
            # Checks if desired position is up a row and up left at a diagonal.
            temp = self._board[self._board.index(move_from) + 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 19 == self._board.index(move_to):
            # Checks if desired position is up a row and up right at a diagonal.
            temp = self._board[self._board.index(move_from) + 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 17 == self._board.index(move_to):
            # Checks if desired position is down a row and down right at a diagonal.
            temp = self._board[self._board.index(move_from) - 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 19 == self._board.index(move_to):
            # Checks if desired position is down a row and down left at a diagonal.
            temp = self._board[self._board.index(move_from) - 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 11 == self._board.index(move_to):
            # Checks if desired position is to the right and up at a diagonal.
            temp = self._board[self._board.index(move_from) + 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 7 == self._board.index(move_to):
            # Checks if desired position is to the right and down at a diagonal.
            temp = self._board[self._board.index(move_from) + 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 7 == self._board.index(move_to):
            # Checks if desired position is to the left and up at a diagonal.
            temp = self._board[self._board.index(move_from) - 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 11 == self._board.index(move_to):
            # Checks if desired position is to the left and down at a diagonal.
            temp = self._board[self._board.index(move_from) - 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "red"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "red horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        else:
            return False

    def move_red_chariot(self, move_from, move_to):
        """Function to move red player's chariot."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif self._board.index(move_to) - self._board.index(move_from) % 9 == 0:  # Checks if move is vertical.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is up vertically.
                temp = self._board.index(move_from) + 9  # Establishes temp variable as next position in line.
                return self.move_chariot_up(move_from, move_to, temp)  # Utilizes move chariot up function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is down vertically.
                temp = self._board.index(move_from) - 9  # Establishes temp variable as next position in line.
                return self.move_chariot_down(move_from, move_to, temp)  # Utilizes move chariot down function for move.
        elif self._board.index(move_to) - self._board.index(move_from) % 9 != 0:  # Checks if move is horizontal.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is to the right.
                temp = self._board.index(move_from) + 1  # Establishes temp variable as next position in line.
                return self.move_chariot_right(move_from, move_to,
                                               temp)  # Utilizes move chariot right function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is to the left.
                temp = self._board.index(move_from) - 1  # Establishes temp variable as next position in line.
                return self.move_chariot_left(move_from, move_to, temp)  # Utilizes move chariot left function for move.
        else:
            return False

    def move_red_cannon(self, move_from, move_to):
        """Function to move red player's cannon."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif self._board.index(move_to) - self._board.index(move_from) % 9 == 0:  # Checks if move is vertical.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is up vertically.
                temp = self._board.index(move_from) + 9  # Establishes temp variable as next position in line.
                return self.move_cannon_up(move_from, move_to, temp)  # Utilizes move chariot up function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is down vertically.
                temp = self._board.index(move_from) - 9  # Establishes temp variable as next position in line.
                return self.move_cannon_down(move_from, move_to, temp)  # Utilizes move chariot down function for move.
        elif self._board.index(move_to) - self._board.index(move_from) % 9 != 0:  # Checks if move is horizontal.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is to the right.
                temp = self._board.index(move_from) + 1  # Establishes temp variable as next position in line.
                return self.move_cannon_right(move_from, move_to,
                                              temp)  # Utilizes move chariot right function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is to the left.
                temp = self._board.index(move_from) - 1  # Establishes temp variable as next position in line.
                return self.move_cannon_left(move_from, move_to, temp)  # Utilizes move chariot left function for move.
        else:
            return False

    def move_red_soldier(self, move_from, move_to):
        """Function to move red player's soldier."""
        if "red" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif move_to in self._red_zone:  # Checks if desired position is on red's side of the river.
            if self._board.index(move_from) + 9 == self._board.index(move_to):
                # Checks if desired position is one row down vertically from current position.
                if self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "black general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                else:
                    return False
        elif move_to in self._black_zone:  # Checks if desired position is on black's side of the river.
            if self._board.index(move_from) + 1 == self._board.index(move_to):
                if self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "black general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            elif self._board.index(move_from) - 1 == self._board.index(move_to):
                # Checks if desired position is one position to the left of current position.
                if self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "black general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            elif self._board.index(move_from) + 9 == self._board.index(move_to):
                if self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "black general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            else:
                return False

    def move_black_general(self, move_from, move_to):
        """Function to move black's general."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif move_to not in self._black_palace:  # Checks if desired position is in black player's palace.
            return False
        elif self._board.index(move_from) + 9 == self._board.index(move_to):
            #  Checks if desired position is one position vertically down of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_from] = "black general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 9 == self._board.index(move_to):
            #  Checks if desired position is one position vertically up of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_from] = "black general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) + 1 == self._board.index(move_to):
            # Checks if desired position is one position to the right of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_from] = "black general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 1 == self._board.index(move_to):
            # Checks if desired position is one position to the left of current position.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""  # Previous position becomes empty.
            XiangqiGame._red_general = move_to
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_from] = "black general"
                self._game_board[move_to] = ""
                XiangqiGame._red_general = move_from
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        else:
            return False

    def move_black_guard(self, move_from, move_to):
        """Function to move black's guard."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif move_to not in self._black_palace:  # Checks if desired position is within black player's palace.
            return False
        elif self._board.index(move_from) + 10 == self._board.index(move_to):
            # Checks if desired position is down a row diagonally to the right.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "black guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 10 == self._board.index(move_to):
            # Checks if desired position is up one row diagonally to the left.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "black guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) + 8 == self._board.index(move_to):
            # Checks if desired position is down one row diagonally to the left.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "black guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._board.index(move_from) - 8 == self._board.index(move_to):
            # Checks if desired position is up one row diagonally to the right.
            self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
            self._game_board[move_from] = ""
            if XiangqiGame.is_in_check(self, "black"):
                self._game_board[move_to] = ""
                self._game_board[move_from] = "black guard"
                return False
            else:
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        else:
            return False

    def move_black_elephant(self, move_from, move_to):
        """Function to move black's elephant."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif move_to in self._red_zone:  # Checks if desired position is on red's side of the river.
            return False
        elif self._board.index(move_from) + 16 == self._board.index(move_to):
            # Checks if desired position is down two rows diagonally to the left.
            temp = self._board[self._board.index(move_from) + 8]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 16 == self._board.index(move_to):
            # Checks if desired position is up two rows diagonally to the right.
            temp = self._board[self._board.index(move_from) - 8]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 20 == self._board.index(move_to):
            # Checks if desired position is down two rows diagonally to the right.
            temp = self._board[self._board.index(move_from) + 10]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 20 == self._board.index(move_to):
            # Checks if desired position is up two rows diagonally to the left.
            temp = self._board[self._board.index(move_from) - 10]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black elephant"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        else:
            return False

    def move_black_horse(self, move_from, move_to):
        """Function to move black's horse."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif self._board.index(move_from) + 17 == self._board.index(move_to):
            # Checks if desired position is up a row and up left at a diagonal.
            temp = self._board[self._board.index(move_from) + 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 19 == self._board.index(move_to):
            # Checks if desired position is up a row and up right at a diagonal.
            temp = self._board[self._board.index(move_from) + 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 17 == self._board.index(move_to):
            # Checks if desired position is down a row and down right at a diagonal.
            temp = self._board[self._board.index(move_from) - 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 19 == self._board.index(move_to):
            # Checks if desired position is down a row and down left at a diagonal.
            temp = self._board[self._board.index(move_from) - 9]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 11 == self._board.index(move_to):
            # Checks if desired position is to the right and up at a diagonal.
            temp = self._board[self._board.index(move_from) + 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 7 == self._board.index(move_to):
            # Checks if desired position is to the right and down at a diagonal.
            temp = self._board[self._board.index(move_from) + 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) + 7 == self._board.index(move_to):
            # Checks if desired position is to the left and up at a diagonal.
            temp = self._board[self._board.index(move_from) - 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        elif self._board.index(move_from) - 11 == self._board.index(move_to):
            # Checks if desired position is to the left and down at a diagonal.
            temp = self._board[self._board.index(move_from) - 1]  # Establishes variable for place to be skipped.
            if "red" in self._game_board[temp] or "black" in self._game_board[temp]:
                # Checks if place to be skipped is occupied.
                return False
            elif self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""
                if XiangqiGame.is_in_check(self, "black"):
                    self._game_board[move_to] = ""
                    self._game_board[move_from] = "black horse"
                    return False
                else:
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
        else:
            return False

    def move_black_chariot(self, move_from, move_to):
        """Function to move black's chariot."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif self._board.index(move_to) - self._board.index(move_from) % 9 == 0:  # Checks if move is vertical.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is up vertically.
                temp = self._board.index(move_from) + 9  # Establishes temp variable as next position in line.
                return self.move_chariot_up(move_from, move_to, temp)  # Utilizes move chariot up function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is down vertically.
                temp = self._board.index(move_from) - 9  # Establishes temp variable as next position in line.
                return self.move_chariot_down(move_from, move_to, temp)  # Utilizes move chariot down function for move.
        elif self._board.index(move_to) - self._board.index(move_from) % 9 != 0:  # Checks if move is horizontal.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is to the right.
                temp = self._board.index(move_from) + 1  # Establishes temp variable as next position in line.
                return self.move_chariot_right(move_from, move_to,
                                               temp)  # Utilizes move chariot right function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is to the left.
                temp = self._board.index(move_from) - 1  # Establishes temp variable as next position in line.
                return self.move_chariot_left(move_from, move_to, temp)  # Utilizes move chariot left function for move.
        else:
            return False

    def move_black_cannon(self, move_from, move_to):
        """Function to move black's cannon."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by red piece.
            return False
        elif self._board.index(move_to) - self._board.index(move_from) % 9 == 0:  # Checks if move is vertical.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is up vertically.
                temp = self._board.index(move_from) + 9  # Establishes temp variable as next position in line.
                return self.move_cannon_up(move_from, move_to, temp)  # Utilizes move chariot up function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is down vertically.
                temp = self._board.index(move_from) - 9  # Establishes temp variable as next position in line.
                return self.move_cannon_down(move_from, move_to, temp)  # Utilizes move chariot down function for move.
        elif self._board.index(move_to) - self._board.index(move_from) % 9 != 0:  # Checks if move is horizontal.
            if self._board.index(move_to) > self._board.index(move_from):  # Checks if move is to the right.
                temp = self._board.index(move_from) + 1  # Establishes temp variable as next position in line.
                return self.move_cannon_right(move_from, move_to,
                                              temp)  # Utilizes move chariot right function for move.
            elif self._board.index(move_to) < self._board.index(move_from):  # Checks if move is to the left.
                temp = self._board.index(move_from) - 1  # Establishes temp variable as next position in line.
                return self.move_cannon_left(move_from, move_to, temp)  # Utilizes move chariot left function for move.
        else:
            return False

    def move_black_soldier(self, move_from, move_to):
        """Function to move black's soldier."""
        if "black" in self._game_board[move_to]:  # Checks if desired position is already occupied by black piece.
            return False
        elif move_to in self._black_zone:  # Checks if desired position is within black's side of the river.
            if self._board.index(move_from) - 9 == self._board.index(move_to):
                # Checks if desired position is up one row vertically from current position.
                if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "red general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            else:
                return False
        elif move_to in self._red_zone:  # Checks if desired position is on red's side of the river.
            if self._board.index(move_from) + 1 == self._board.index(move_to):
                # Checks if desired position is one position to the right of current position.
                if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "red general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            elif self._board.index(move_from) - 1 == self._board.index(move_to):
                # Checks if desired position is one piece to the left of current position.
                if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "red general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            elif self._board.index(move_from) - 9 == self._board.index(move_to):
                # Checks if desired position is down one row vertically on red's side of the river.
                if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                    XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
                elif self._game_board[move_to] != "red general":
                    self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                    self._game_board[move_from] = ""  # Previous position becomes empty.
                    self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                    return True
            else:
                return False

    def move_chariot_right(self, move_from, move_to, temp):
        """Function to move chariot piece to right."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp + 1  # Establishes variable as the next position in line.
            return self.move_chariot_right(move_from, move_to, temp_new)  # Recursion to check next position in line.
        else:
            return False

    def move_chariot_left(self, move_from, move_to, temp):
        """Function to move chariot piece to the left."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp - 1  # Establishes variable as the next position in line.
            return self.move_chariot_left(move_from, move_to, temp_new)  # Recursion to check next position in line.
        else:
            return False

    def move_chariot_down(self, move_from, move_to, temp):
        """Function to move chariot piece down."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp - 9  # Establishes variable as the next position in line.
            return self.move_chariot_down(move_from, move_to, temp_new)  # Recursion to check next position in line.
        else:
            return False

    def move_chariot_up(self, move_from, move_to, temp):
        """Function to move chariot piece up."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp + 9  # Establishes variable as the next position in line.
            return self.move_chariot_up(move_from, move_to, temp_new)  # Recursion to check next position in line.
        else:
            return False

    def move_cannon_right(self, move_from, move_to, temp, jump=0):
        """Function to move cannon piece to right."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp + 1  # Establishes variable as the next position in line.
            return self.move_cannon_right(move_from, move_to, temp_new)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump == 0:
            # Checks if next position is occupied and if cannon piece has not jumped another piece yet.
            jump += 1  # Increases jump count by 1
            temp_new = temp + 1  # Establishes variable as the next position in line.
            return self.move_cannon_right(move_from, move_to, temp_new,
                                          jump)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump > 0:
            # Checks if next position is occupied and if cannon piece has already jumped another piece.
            return False
        else:
            return False

    def move_cannon_left(self, move_from, move_to, temp, jump=0):
        """Function to move cannon piece to the left."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp - 1  # Establishes variable as the next position in line.
            return self.move_cannon_left(move_from, move_to, temp_new)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump == 0:
            # Checks if next position is occupied and if cannon piece has not jumped another piece yet.
            jump += 1  # Increases jump count by 1
            temp_new = temp - 1  # Establishes variable as the next position in line.
            return self.move_cannon_left(move_from, move_to, temp_new,
                                         jump)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump > 0:
            # Checks if next position is occupied and if cannon piece has already jumped another piece.
            return False
        else:
            return False

    def move_cannon_down(self, move_from, move_to, temp, jump=0):
        """Function to move cannon piece down."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp - 9  # Establishes variable as the next position in line.
            return self.move_cannon_down(move_from, move_to, temp_new)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump == 0:
            # Checks if next position is occupied and if cannon piece has not jumped another piece yet.
            jump += 1  # Increases jump count by 1
            temp_new = temp - 9  # Establishes variable as the next position in line.
            return self.move_cannon_down(move_from, move_to, temp_new,
                                         jump)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump > 0:
            # Checks if next position is occupied and if cannon piece has already jumped another piece.
            return False
        else:
            return False

    def move_cannon_up(self, move_from, move_to, temp, jump=0):
        """Function to move cannon piece up."""
        if temp == self._board.index(move_to):  # Checks if temp variable equal position to move to.
            if self._game_board[move_to] == "red general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "BLACK_WON"  # Changes game state to black Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            elif self._game_board[move_to] == "black general":  # Checks if position to be moved to contains general.
                XiangqiGame._game_state = "RED_WON"  # Changes game state to Red Won.
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
            else:
                self._game_board[move_to] = self._game_board[move_from]  # Places piece in desired position.
                self._game_board[move_from] = ""  # Previous position becomes empty.
                self._move_counter += 1  # Increase move counter by one to aide in identifying correct players turn.
                return True
        elif self._game_board[self._board[temp]] == "":  # Checks if next position in line is not occupied.
            temp_new = temp + 9  # Establishes variable as the next position in line.
            return self.move_cannon_up(move_from, move_to, temp_new)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump == 0:
            # Checks if next position is occupied and if cannon piece has not jumped another piece yet.
            jump += 1  # Increases jump count by 1
            temp_new = temp + 9  # Establishes variable as the next position in line.
            return self.move_cannon_up(move_from, move_to, temp_new, jump)  # Recursion to check next position in line.
        elif "black" in self._game_board[self._board[temp]] or "red" in self._game_board[self._board[temp]] and jump > 0:
            # Checks if next position is occupied and if cannon piece has already jumped another piece.
            return False
        else:
            return False


class XiangqiGame(Pieces):
    """Represents Xiangqi Game (Chinese Chess), inheriting from Pieces."""

    def __init__(self):
        super().__init__()
        self._game_board = {"a1": "red chariot", "b1": "red horse", "c1": "red elephant", "d1": "red guard",
                            "e1": "red general", "f1": "red guard", "g1": "red elephant", "h1": "red horse",
                            "i1": "red chariot",
                            "a2": "", "b2": "", "c2": "", "d2": "", "e2": "", "f2": "", "g2": "", "h2": "", "i2": "",
                            "a3": "", "b3": "red cannon", "c3": "", "d3": "", "e3": "", "f3": "", "g3": "",
                            "h3": "red cannon", "i3": "",
                            "a4": "red soldier", "b4": "", "c4": "red soldier", "d4": "", "e4": "red soldier",
                            "f4": "",
                            "g4": "red soldier", "h4": "", "i4": "red soldier",
                            "a5": "", "b5": "", "c5": "", "d5": "", "e5": "", "f5": "", "g5": "", "h5": "", "i5": "",
                            "a6": "", "b6": "", "c6": "", "d6": "", "e6": "", "f6": "", "g6": "", "h6": "", "i6": "",
                            "a7": "black soldier", "b7": "", "c7": "black soldier", "d7": "",
                            "e7": "black soldier",
                            "f7": "", "g7": "black soldier", "h7": "", "i7": "black soldier",
                            "a8": "", "b8": "black cannon", "c8": "", "d8": "", "e8": "", "f8": "", "g8": "",
                            "h8": "black cannon", "i8": "",
                            "a9": "", "b9": "", "c9": "", "d9": "", "e9": "", "f9": "", "g9": "", "h9": "", "i9": "",
                            "a10": "black chariot", "b10": "black horse", "c10": "black elephant",
                            "d10": "black guard",
                            "e10": "black general", "f10": "black guard", "g10": "black elephant",
                            "h10": "black horse",
                            "i10": "black chariot"}  # Initializes game board with pieces in correct places.
        self._game_state = "UNFINISHED"  # Initializes game state.
        self._move_counter = 1  # Initializes what move it is to aide in identifying correct player piece.
        self._black_general = "e10"
        self._red_general = "e1"

    def get_game_state(self):
        """Functions used to retrieve the current game state."""
        return self._game_state  # Returns game state.

    def is_in_check(self, player):
        """Function to check if player is in check."""
        if player.upper() == "RED":  # Checks if player chosen is red.
            return self.is_red_check()  # Utilizes is red check function.
        elif player.upper() == "BLACK":  # Checks if player chosen is black.
            return self.is_black_check()  # Utilizes is black check function.

    def make_move(self, move_from, move_to):
        """Function to move player piece utilizing current position and desired positioned."""
        if move_from not in self._game_board or move_to not in self._game_board:
            # Checks if selected position is on the board or if the desired position is on the board.
            return False
        else:
            return Pieces.identify_piece(self, move_from, move_to)  # Utilizes pieces class function to initiate move.

    def display_board(self):
        """Function that produces board with current positions."""
        return self._game_board  # Returns said board.

    def is_red_check(self):
        """Helper function to check if red player is in check."""
        if self._game_state == "BLACK_WON":  # Checks if game state is black won.
            return True
        elif self._game_state == "RED_WON":  # Checks if game state is red won.
            return False
        for key in self._game_board.items():  # Iterates through game board.
            if "black soldier" in key:  # Checks if black soldier is within game board.
                if self.move_black_soldier(key[0], self._red_general):  # Checks if general is in check by soldier
                    return True
                else:
                    continue
            elif "black horse" in key:  # Checks if black horse is within game board.
                if self.move_black_horse(key[0], self._red_general):  # Checks if general is in check by horse.
                    return True
                else:
                    continue
            elif "black chariot" in key:  # Checks if black chariot is within game board.
                if self.move_black_chariot(key[0], self._red_general):  # Checks if general is in check by chariot.
                    return True
                else:
                    continue
            elif "black cannon" in key:  # Checks if black cannon is within game board.
                if self.move_black_cannon(key[0], self._red_general):  # Checks if general is in check by
                    return True
                else:
                    continue
            else:
                return False

    def is_black_check(self):
        """Helper function to check if black player is in check."""
        if self._game_state == "RED_WON":  # Checks if game state is red won.
            return True
        elif self._game_state == "BLACK_WON":  # Checks if game state is black won.
            return False
        for key in self._game_board.items():  # Iterates through game board.
            if "red soldier" in key:  # Checks if red soldier on game board.
                if self.move_red_soldier(key[0], self._black_general):  # Checks if general is check by red soldier.
                    return True
                else:
                    continue
            elif "red horse" in key:  # Checks if red horse on game board.
                if self.move_red_horse(key[0], self._black_general):  # Checks if general is in check by red horse.
                    return True
                else:
                    continue
            elif "red chariot" in key:  # Checks if red chariot on game board.
                if self.move_red_chariot(key[0], self._black_general):  # Checks if general is in check by red chariot.
                    return True
                else:
                    continue
            elif "red cannon" in key:  # Checks if red cannon on game board.
                if self.move_red_cannon(key[0], self._black_general):  # Checks if general is in check by red cannon.
                    return True
                else:
                    continue
            else:
                return False
