using EmployeeHelper.Domain;
using EmployeeHelper.Infrastructure.Abstractions;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace EmployeeHelper.Infrastructure.DataAccess;

public class AppDbContext : IdentityDbContext<User, Role, Guid>, IAppDbContext
{
    public DbSet<Role> Roles { get; private set; }

    public DbSet<User> Users { get; private set; }

	public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) 
    { 
    }

    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);
    }
}
