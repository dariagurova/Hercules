/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dgurova <dariagurova91@gmail.com>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/01 22:18:23 by dgurova           #+#    #+#             */
/*   Updated: 2018/03/02 13:39:36 by dgurova          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <pthread.h>

# define BUFF_SIZE (1024)

void	error(char *str)
{
	printf("%s\n", str);
	exit(1);
}

int		main(int ac, char *av[])
{
	struct sockaddr_in	addr;
	socklen_t			len;
	int					serv_fd;
	int					client_fd;
	int					Nread;
	char				buf[BUFF_SIZE + 1];

	if(ac != 2)
		error("Usage: ./server [port]\n");
	client_fd = socket(AF_INET, SOCK_STREAM, 0);
	if (client_fd == -1)
		error("socket() failed");
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = INADDR_ANY;
	addr.sin_port = htons(atoi(av[1]));
	if (bind(client_fd, (struct sockaddr *)&addr, sizeof(addr)) != 0)
		error("bind() failed\n");
	while (1)
	{
		if (listen(client_fd, 10) < 0)
			error("listen() failed\n");
		if ((serv_fd = accept(client_fd, (struct sockaddr *)&addr, &len)) < 0)
			error("accept() failed\n");
		while ((Nread = recv(serv_fd, buf, BUFF_SIZE, 0)) > 0)
		{
			buf[Nread] = '\0';
			if (strncmp(buf, "ping", 5) == 0)
				write(serv_fd, "pong pong", 9);
			else if (strncmp(buf, "q", 1) == 0)
				error("Stop server.");
			else
				write(serv_fd, "\0", 1);
		}
		close(serv_fd);
	}
	close(client_fd);
	return (0);
}
