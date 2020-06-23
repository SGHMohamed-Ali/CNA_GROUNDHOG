##
## EPITECH PROJECT, 2019
## groundhog
## File description:
## groundhog
##

NAME	= groundhog

RM	= rm -f

SRCS	= script.sh

all: $(NAME)

$(NAME):
	cp $(SRCS) $(NAME)

clean:
	$(RM) $(NAME)

fclean: clean

re: fclean all

.PHONY: all clean fclean re
