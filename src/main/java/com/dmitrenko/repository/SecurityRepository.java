package com.dmitrenko.repository;

import com.dmitrenko.domain.Security;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SecurityRepository extends JpaRepository<Security, String> {
}
