package com.mobileforce.hometeach.data.sources.local.dao

import androidx.lifecycle.LiveData
import androidx.room.*
import com.mobileforce.hometeach.data.sources.local.entities.CardEntity
import com.mobileforce.hometeach.data.sources.local.entities.ProfileEntity
import com.mobileforce.hometeach.data.sources.local.entities.UserEntity

@Dao
interface UserDao {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun saveUser(user: UserEntity)

    @Query("SELECT * FROM user")
    fun getUser(): LiveData<UserEntity>

    @Delete
    fun deleteUser(user: UserEntity)

    @Query("DELETE FROM user")
    suspend fun clearDb()

    @Query("SELECT * FROM user")
    suspend fun getSingleUser(): UserEntity

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun saveUserProfile(profile: ProfileEntity)

    @Query("SELECT * FROM profile")
    suspend fun getUserProfile(): ProfileEntity

    @Query("SELECT * FROM profile")
    fun observeableProfileData(): LiveData<ProfileEntity>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun saveCard(card: CardEntity)

    @Query("SELECT * FROM user_card")
    fun observeUserCards(): LiveData<List<CardEntity>>

}