'use client';

import Link from 'next/link';
import { cn } from "@/lib/utils";
import { usePathname } from 'next/navigation';

interface MenuItemProps {
  href: string;
  protected?: boolean;
  isAuthenticated?: boolean;
  onProtectedClick: (_e: React.MouseEvent, _href: string) => void;
  onClick?: () => void;
  children: React.ReactNode;
}

const MenuItem = ({ children, href, protected: isProtected, isAuthenticated, onProtectedClick, onClick }: MenuItemProps) => {
  const pathname = usePathname();
  const isActive = pathname === href;

  const handleClick = (e: React.MouseEvent) => {
    if (isProtected && !isAuthenticated) {
      onProtectedClick(e, href);
    }
    onClick?.();
  };

  return (
    <Link
      href={href}
      onClick={handleClick}
      className={cn(
        "flex items-center gap-2",
        "px-3 py-2 rounded-md text-sm",
        "transition-colors duration-200",
        "text-muted-foreground hover:text-foreground",
        "hover:bg-muted",
        isActive && "text-primary font-medium bg-muted"
      )}
    >
      {children}
    </Link>
  );
};

export type { MenuItemProps };
export default MenuItem; 