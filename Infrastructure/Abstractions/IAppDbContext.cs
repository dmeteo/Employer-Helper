using EmployeeHelper.Domain;
using Microsoft.EntityFrameworkCore;

namespace EmployeeHelper.Infrastructure.Abstractions;

public interface IAppDbContext
{
	DbSet<User> Users { get; }

	DbSet<Role> Roles { get; }
}
