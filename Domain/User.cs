using Microsoft.AspNetCore.Identity;

namespace EmployeeHelper.Domain
{
    public class User : IdentityUser<Guid>
    {
        public string FirstName {  get; set; }

        public string LastName { get; set; }

        public string Surname { get; set; }

    }
}
